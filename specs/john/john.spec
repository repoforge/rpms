# $Id$
# Authority: dag

Summary: John the Ripper password cracker
Name: john
Version: 1.7.0.2
Release: 1
License: GPL
Group: Applications/System
URL: http://www.openwall.com/john/

Source: http://www.openwall.com/john/f/john-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
John the Ripper is a fast password cracker. Its primary purpose is to
detect weak Unix passwords, but a number of other hash types are
supported as well.

%prep
%setup

%{__perl} -pi.orig -e '
		s|^#define CFG_NAME .*$|#define CFG_NAME "/etc/john.conf"|;
		s|^#define WORDLIST_NAME .*$|#define WORDLIST_NAME "/usr/share/john/password.lst"|;
	' src/params.h
%{__perl} -pi.orig -e 's|ile = ~/|ile = /usr/share/john/|' run/john.conf

%build
%{__make} %{?_smp_mflags} -C src clean \
%ifarch %{ix86}
				linux-x86-mmx
%endif
%ifarch x86_64
				linux-x86-64
%endif
%ifarch alpha
				linux-alpha
%endif
%ifarch sparc
				linux-alpha
%endif
%ifarch ppc
				linux-ppc32
%endif
%ifarch ppc64
				linux-ppc64
%endif

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 run/john.conf %{buildroot}%{_sysconfdir}/john.ini
%{__install} -Dp -m0755 run/john %{buildroot}%{_bindir}/john
%{__install} -Dp -m0755 run/mailer %{buildroot}%{_bindir}/mailer

%{__install} -d -m0755 %{buildroot}%{_datadir}/john/
%{__install} -p -m0644 run/*.chr run/password.lst %{buildroot}%{_datadir}/john/
%{__ln_s} -f john %{buildroot}%{_bindir}/unafs
%{__ln_s} -f john %{buildroot}%{_bindir}/unique
%{__ln_s} -f john %{buildroot}%{_bindir}/unshadow

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/*
%config(noreplace) %{_sysconfdir}/john.ini
%{_bindir}/*
%{_datadir}/john/

%changelog
* Sun May 28 2006 Dag Wieers <dag@wieers.com> - 1.7.0.2-1
- Updated to release 1.7.0.2.

* Sun Aug 17 2003 Dag Wieers <dag@wieers.com> - 1.6-0
- Initial package. (using DAR)
