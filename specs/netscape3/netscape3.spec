# $Id$
# Authority: dag

# ExcludeDist: el5

Summary: The Netscape standalone navigator
Name: netscape3
Version: 3.04
Release: 0.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.netscape.com/

ExclusiveArch: i386
Source: ftp://ftp.netscape.com/pub/communicator/english/%{version}/unix/unsupported/linux12/navigator_standalone/netscape-v304-us.x86-unknown-linux-elf.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Netscape Navigator is a Web browser which supports HTML
standards, Java, JavaScript and some style sheets.

%prep
%setup -c

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m755 netscape %{buildroot}%{_libdir}/netscape-%{version}/netscape
%{__install} -Dp -m755 java_301 %{buildroot}%{_libdir}/netscape-%{version}/java_301

%{__install} -d -m0755 %{buildroot}/%{_bindir}/
%{__ln_s} -f %{_libdir}/netscape-%{version}/netscape %{buildroot}%{_bindir}/netscape-%{version}
%{__ln_s} -f %{_libdir}/netscape-%{version}/netscape %{buildroot}%{_bindir}/netscape

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README
%{_bindir}/*
%{_libdir}/netscape-%{version}/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 3.04-0.2
- Rebuild for Fedora Core 5.

* Thu Jan 02 2002 Dag Wieers <dag@wieers.com> - 3.04
- Initial package.
