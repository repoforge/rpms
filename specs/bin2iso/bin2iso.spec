# $Id$
# Authority: dries
# Upstream: Bob Doiron

%define real_version 19b

Summary: Convert bin/cue images to iso images or wav files
Name: bin2iso
Version: 1.9
Release: 0.b.2%{?dist}
License: Unknown, Freely distributable
Group: Applications/File
URL: http://users.andara.com/~doiron/bin2iso/

Source: http://users.eastlink.ca/~doiron/bin2iso/linux/bin2iso%{real_version}_linux.c
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Bin2iso converts bin/cue images to iso images.or wav files.

%prep
%setup -c -T

%build
%{__cc} -Wall %{SOURCE0} -o bin2iso

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 bin2iso %{buildroot}%{_bindir}/bin2iso

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/bin2iso

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.9-0.b.2
- Rebuild for Fedora Core 5.

* Tue Sep 13 2005 Dries Verachtert <dries@ulyssis.org> - 1.9-0.b
- Initial package.
