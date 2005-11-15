# $Id$
# Authority: dries
# Upstream: <herrekberg$users,sourceforge,net>

Summary: Comic book viewer
Name: comix
Version: 1.6
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://comix.sourceforge.net/

Source: http://dl.sf.net/comix/comix-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
BuildRequires: python
Requires: python

%description
Comix is a comic book viewer. It reads zip, rar, tar, tar.gz, and tar.bz2 
archives (often called .cbz, .cbr and .cbt) as well as normal image files.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_prefix}
python install.py install --installdir %{buildroot}%{_prefix}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README
%doc %{_mandir}/man1/comix*
%{_bindir}/comix
%{_datadir}/pixmaps/comix.png
%{_datadir}/applications/*comix.desktop

%changelog
* Mon Nov 07 2005 Dries Verachtert <dries@ulyssis.org> - 1.6-1
- Initial package.
