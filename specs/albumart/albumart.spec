# $Id$

# Authority: dag

Summary: Downloads album cover images semi-automatically from the Internet
Name: albumart
Version: 1.1
Release: 0
License: GPL
Group: Applications/Internet
URL: http://kempele.fi/~skyostil/projects/albumart/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://louhi.kempele.fi/~skyostil/projects/albumart/dist/albumart-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


Requires: python, PyQt, python-imaging
BuildArch: noarch

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
python setup.py install \
	--root="%{buildroot}" \
	--record="INSTALLED_FILES"

%clean
%{__rm} -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-, root, root, 0755)

%changelog
* Mon Jun 30 2003 Dag Wieers <dag@wieers.com> - 1.1-0
- Initial package. (using DAR)
