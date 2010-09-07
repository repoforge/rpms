# $Id$
# Authority: dag

Summary: Alter MIME-encoded mailpacks
Name: altermime
Version: 0.3.10
Release: 1%{?dist}
License: BSD
Group: Applications/Internet
URL: http://www.pldaniels.com/altermime/

Source: http://www.pldaniels.com/altermime/altermime-%{version}.tar.gz
Patch: altermime-0.3.10-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
altermime is a small program which is used to alter MIME-encoded mailpacks.

altermime can insert disclaimers, insert arbitary X-headers, modify existing
headers, remove attachments based on filename or content-type and replace
attachments based on filename.

%prep
%setup -q
%patch -p1

%build
%{__make} CC="%{__cc}" 


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
* Tue Sep 07 2010 David Hrbáč <david@hrbac.cz> - 0.3.10-1
- new upstream release
- patch to build

* Tue Jul 21 2009 Dag Wieers <dag@wieers.com> - 0.3.9-1
- Updated to release 0.3.9.

* Mon Jan 28 2008 Dag Wieers <dag@wieers.com> - 0.3.7-1
- Initial package. (using DAR)
