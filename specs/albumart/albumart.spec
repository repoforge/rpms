# $Id$
# Authority: dag

Summary: Downloads album cover images semi-automatically from the Internet
Name: albumart
Version: 1.1
Release: 0.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://kempele.fi/~skyostil/projects/albumart/

Source: http://louhi.kempele.fi/~skyostil/projects/albumart/dist/albumart-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python, python-devel
Requires: python, PyQt, python-imaging

%description
Album Cover Art Downloader is a download utility for semi-automatically
downloading matching cover images from Amazon.com for each album in your
music collection. It saves the cover images so that they will be
automatically used by programs such as Konqueror, various XMMS plugins,
Windows Media Player, etc.

%prep
%setup

%build
python setup.py build

%install
%{__rm} -rf %{buildroot}
python setup.py install --root="%{buildroot}"

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_docdir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README TODO
%{_bindir}/albumart-qt
%{_datadir}/albumart/
%{_datadir}/applnk/Multimedia/albumart.desktop
%{_datadir}/pixmaps/albumart.png
%{_libdir}/albumart/

%changelog
* Mon Jun 30 2003 Dag Wieers <dag@wieers.com> - 1.1-0
- Initial package. (using DAR)
