# $Id$
# Authority: dag
# Upstream: Chris Ladd <caladd$particlestorm,net>

Summary: Post entries to a Blosxom based weblog
Name: gnome-blosxom
Version: 1.0
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://gnome-blosxom.sourceforge.net/

Source: http://dl.sf.net/gnome-blosxom/gnome-blosxom-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python >= 2.0, pygtk2-devel, gnome-python2
Requires: python >= 2.0, pygtk2, gnome-python2

%description
Gnome Bloxsom is a GUI based program to post entries to a Blosxom
based weblog.

%prep
%setup

%build
%{__make} \
	datadir="%{_datadir}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/gnome-blosxom
%{_datadir}/pixmaps/gnome-blosxom.png
%{_datadir}/applications/gnome-blosxom.desktop

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-1.2
- Rebuild for Fedora Core 5.

* Sat Aug 28 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package contributed by Chris Ladd.
