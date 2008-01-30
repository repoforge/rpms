# $Id$
# Authority: dag

Summary: Alter MIME-encoded mailpacks
Name: altermime
Version: 0.3.7
Release: 1
License: BSD
Group: Applications/Internet
URL: http://www.pldaniels.com/altermime/

Source: http://www.pldaniels.com/altermime/altermime-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
altermime is a small program which is used to alter MIME-encoded mailpacks.

altermime can insert disclaimers, insert arbitary X-headers, modify existing
headers, remove attachments based on filename or content-type and replace
attachments based on filename.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 altermime %{buildroot}%{_bindir}/altermime

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG LICENCE README
%{_bindir}/altermime

%changelog
* Mon Jan 28 2008 Dag Wieers <dag@wieers.com> - 0.3.7-1
- Initial package. (using DAR)
