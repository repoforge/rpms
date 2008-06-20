# $Id$
# Authority: fabian
# Upstream: 

Summary: Mailfeeder is a tool designed to inject a mailpack back into a MTA
Name: mailfeeder
Version: 0.2.5
Release: 1
License: GPL
Group: Applications/Internet
URL: http://pldaniels.com/mailfeeder/

Source: http://pldaniels.com/mailfeeder/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description

Mailfeeder is a tool designed to inject a mailpack back into a MTA (mail server, ie, Sendmail, Postfix) using socket calls. Currently it is used in a variety of projects such as Inflex and Xamime to perform post-filtered queue injection or delivery.

%prep
%setup
%build
%{__make} %{?_smp_mflags}

%install

%{__install} -m0755 -d %{buildroot}/usr/sbin
%{__install} -m0755 mailfeeder %{buildroot}/usr/sbin
%{__install} -m0755 -d %{buildroot}/usr/share/man/man1
%{__install} -m0755 mailfeeder.1 %{buildroot}/usr/share/man/man1

%post

%postun 

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0755)
%doc INSTALL README
%doc %{_mandir}/man?/*
%{_sbindir}/*


%changelog
* Fri Jun 20 2008 Fabian Arrotin <fabian.arrotin@arrfab.net> 
- Initial package

