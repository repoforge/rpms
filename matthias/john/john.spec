# Authority: dag

Summary: John the Ripper password cracker.
Name: john
Version: 1.6
Release: 0
License: GPL
Group: Applications/System
URL: http://www.openwall.com/john/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.openwall.com/john/dl/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
John the Ripper is a fast password cracker. Its primary purpose is to
detect weak Unix passwords, but a number of other hash types are
supported as well.

%prep
%setup

%{__perl} -pi.orig -e '
		s|^#define CFG_NAME .*$|#define CFG_NAME "/etc/john.ini"|;
		s|^#define WORDLIST_NAME .*$|#define WORDLIST_NAME "/usr/share/john/password.lst"|;
	' src/params.h
%{__perl} -pi.orig -e 's| -m486||' src/Makefile
%{__perl} -pi.orig -e 's|ile = ~/|ile = /usr/share/john/|' run/john.ini

%build
%{__make} %{?_smp_mflags} -C src linux-x86-any-elf

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sysconfdir} \
			%{buildroot}%{_bindir} \
			%{buildroot}%{_datadir}/john/
%{__install} -m0644 run/john.ini %{buildroot}%{_sysconfdir}
%{__install} -m0755 run/john run/mailer %{buildroot}%{_bindir}
%{__install} -m0644 run/*.chr run/password.lst %{buildroot}%{_datadir}/john/
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
* Sun Aug 17 2003 Dag Wieers <dag@wieers.com> - 1.6-0
- Initial package. (using DAR)
