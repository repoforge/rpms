# Authority: newrpms
# Tag: test

%define rname BitTorrent

Summary: BitTorrent is a tool for copying files from one machine to another.
Name: bittorrent
Version: 3.2
Release: 0
License: MIT
Group: Applications/Internet
URL: http://bitconjurer.org/BitTorrent/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://bitconjurer.org/BitTorrent/%{rname}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
BuildRequires: python2
Requires: wxPythonGTK

%description
BitTorrent is a tool for copying files from one machine to
another. FTP punishes sites for being popular. Since all uploading is
done from one place, a popular site needs big iron and big
bandwidth. With BitTorrent, clients automatically mirror files they
download, making the publisher's burden almost nothing.

%prep
%setup -n %{rname}-%{version}

%install
%{__rm} -rf %{buildroot}
python2 ./setup.py install --prefix="%{buildroot}%{_prefix}"
%{__perl} -pi -e 's|env python2|env python|' %{buildroot}%{_bindir}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc credits.txt FAQ.txt LICENSE.txt README.txt todo.txt
%{_bindir}/*
%{_libdir}/python*/site-packages/BitTorrent/

%changelog
* Thu Jul 17 2003 Dag Wieers <dag@wieers.com> - 3.2-0
- Initial package. (using DAR)
