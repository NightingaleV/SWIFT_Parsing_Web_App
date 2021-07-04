export function Button({
  children,
  type = 'button',
  shape,
  color,
  icon,
  actionButton,
  className,
  iconName,
  id,
  href = '',
  ...rest
}) {

  const button = (
    <button
      className={classNames(
        'btn',
        className,
        id,
      )}
      type={type}
      {...rest}
    >
      {icon && (
        <i className={classNames(iconName)}>{icon}</i>
      )}
      {children}
    </button>
  );

  const linkButton = (
    <a
      href={href}
      className={classNames(
        'btn',
        className,
        id,
      )}
      {...rest}
    >
      {icon && (
        <i className={classNames(iconName)}>{icon}</i>
      )}
      {children}
    </a>
  );

  // if href prop is present, return link, otherwise button
  return href ? linkButton : button;
}