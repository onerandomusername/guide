import React, { isValidElement } from 'react';
import Head from '@docusaurus/Head';
import Link from '@docusaurus/Link';
import CodeBlock from '@theme/CodeBlock';
import Heading from '@theme/Heading';
import Details from '@theme/Details';
import './styles.css';

import {
	DiscordButton,
	DiscordButtons,
	DiscordEmbed,
	DiscordEmbedField,
	DiscordEmbedFields,
	DiscordInteraction,
	DiscordMarkdown,
	DiscordMention,
	DiscordMessage,
	DiscordMessages,
	DiscordReaction,
	DiscordReactions,
} from '@discord-message-components/react';
import '@discord-message-components/react/styles';
import ResultingCode from '../../components/ResultingCode';

function unwrapMDXElement(element) {
	if (element?.props?.mdxType && element?.props?.originalType) {
		const { mdxType, originalType, ...newProps } = element.props;
		return React.createElement(element.props.originalType, newProps);
	}

	return element;
}

const MDXComponents = {
	head: (props) => {
		const unwrappedChildren = React.Children.map(props.children, (child) => unwrapMDXElement(child));
		return <Head {...props}>{unwrappedChildren}</Head>;
	},
	code: (props) => {
		const { children } = props;

		if (isValidElement(children)) {
			return children;
		}

		return !children.includes('\n') ? <code {...props} /> : <CodeBlock {...props} />;
	},
	a: (props) => <Link {...props} />,
	pre: (props) => {
		const { children } = props;

		if (isValidElement(children) && isValidElement(children?.props?.children)) {
			return children.props.children;
		}

		return <CodeBlock {...(isValidElement(children) ? children?.props : { ...props })} />;
	},
	details: (props) => {
		const items = React.Children.toArray(props.children);

		const summary = items.find((item) => item?.props?.mdxType === 'summary');
		const children = <>{items.filter((item) => item !== summary)}</>;
		return (
			<Details {...props} summary={summary}>
				{children}
			</Details>
		);
	},
	h1: Heading('h1'),
	h2: Heading('h2'),
	h3: Heading('h3'),
	h4: Heading('h4'),
	h5: Heading('h5'),
	h6: Heading('h6'),
	ResultingCode: () => {
		return <ResultingCode />;
	},
	DiscordMessages: (props) => {
		return <DiscordMessages {...props}>{props.children}</DiscordMessages>;
	},
	DiscordMessage: (props) => {
		return <DiscordMessage {...props}>{props.children}</DiscordMessage>;
	},
	DiscordMention: (props) => {
		return <DiscordMention {...props}>{props.children}</DiscordMention>;
	},
	DiscordEmbed: (props) => {
		return <DiscordEmbed {...props}>{props.children}</DiscordEmbed>;
	},
	DiscordEmbedFields: (props) => {
		return <DiscordEmbedFields {...props}>{props.children}</DiscordEmbedFields>;
	},
	DiscordEmbedField: (props) => {
		return <DiscordEmbedField {...props}>{props.children}</DiscordEmbedField>;
	},
	DiscordInteraction: (props) => {
		return <DiscordInteraction {...props}>{props.children}</DiscordInteraction>;
	},
	DiscordMarkdown: (props) => {
		return <DiscordMarkdown {...props}>{props.children}</DiscordMarkdown>;
	},
	DiscordButtons: (props) => {
		return <DiscordButtons {...props}>{props.children}</DiscordButtons>;
	},
	DiscordButton: (props) => {
		return <DiscordButton {...props}>{props.children}</DiscordButton>;
	},
	DiscordReactions: (props) => {
		return <DiscordReactions {...props}>{props.children}</DiscordReactions>;
	},
	DiscordReaction: (props) => {
		return <DiscordReaction {...props}>{props.children}</DiscordReaction>;
	},
};
export default MDXComponents;
