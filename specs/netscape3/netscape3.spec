# $Id$

# Authority: dag

Summary: The Netscape standalone navigator
Name: netscape3
Version: 3.04
Release: 0
License: GPL
Group: Applications/Internet
URL: http://www.netscape.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

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
%{__install} -d -m0755 %{buildroot}%{_libdir}/netscape-%{version}/ \
			%{buildroot}/%{_bindir}/
%{__install} -m755 netscape %{buildroot}%{_libdir}/netscape-%{version}/
%{__install} -m755 java_301 %{buildroot}%{_libdir}/netscape-%{version}/
%{__ln_s} -f %{_libdir}/netscape-%{version}/netscape %{buildroot}%{_bindir}/netscape-%{version}
%{__ln_s} -f %{_libdir}/netscape-%{version}/netscape %{buildroot}%{_bindir}/netscape

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README LICENSE
%{_bindir}/*
%{_libdir}/netscape-%{version}
     
%changelog
* Thu Jan 02 2002 Dag Wieers <dag@wieers.com> - 3.04
- Initial package.
