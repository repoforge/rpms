# $Id$
# Authority: dag
# Upstream: Michel Machado <michel$digirati,com,br>

Summary: Tool to test storage device (flash devices)
Name: f3
%define real_version 1_1_3
Version: 1.1.3
Release: 1%{?dist}
License: GPLv3
Group: Applications/File
URL: http://oss.digirati.com.br/f3/

Source: http://oss.digirati.com.br/f3/f3v%{real_version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Fight Flash Fraud (f3) is a tool to test storage devices (USB, flashcard,
etc...) for errors due to advertising an incorrect capacity.

%prep
%setup -c

%build
%{__cc} %{optflags} -o f3read f3read.c
%{__cc} %{optflags} -o f3write f3write.c

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 f3read %{buildroot}%{_bindir}/f3read
%{__install} -Dp -m0755 f3write %{buildroot}%{_bindir}/f3write

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE
%{_bindir}/f3read
%{_bindir}/f3write

%changelog
* Wed Apr 06 2011 Dag Wieers <dag@wieers.com> - 1.1.3-1
- Initial package. (using DAR)
