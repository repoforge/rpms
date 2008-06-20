# $Id$
# Authority: fabian
# Upstream: PLDaniels Software <pldaniels@gmail.com>

Summary: Tool designed to inject a mailpack back into a MTA
Name: mailfeeder
Version: 0.2.5
Release: 1
License: GPL
Group: Applications/Internet
URL: http://pldaniels.com/mailfeeder/

Source: http://pldaniels.com/mailfeeder/mailfeeder-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Mailfeeder is a tool designed to inject a mailpack back into a MTA
(mail server, ie, Sendmail, Postfix) using socket calls. Currently
it is used in a variety of projects such as Inflex and Xamime to
perform post-filtered queue injection or delivery.

%prep
%setup

%build
%{__make} %{?_smp_mflags} PRF="" CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 mailfeeder %{buildroot}%{_sbindir}/mailfeeder
%{__install} -Dp -m0644 mailfeeder.1 %{buildroot}%{_mandir}/man1/mailfeeder.1

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0755)
%doc CONTRIBUTORS INSTALL* LICENCE README
%doc %{_mandir}/man1/mailfeeder.1*
%{_sbindir}/mailfeeder

%changelog
* Fri Jun 20 2008 Fabian Arrotin <fabian.arrotin@arrfab.net> 0.2.5-1
- Initial package.
