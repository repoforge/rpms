# Authority: dag

# Upstream: 

%define rname WifiScanner

Summary: A tool to discover wireless clients and access points.
Name: wifiscanner
Version: 0.9.1
Release: 0
License: GPL
Group: Applications/Internet
URL: http://wifiscanner.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source:  http://dl.sf.net/WIFIScanner/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

#BuildRequires: 

%description
WifiScanner is a tool to discover wireless clients and access points.

%prep
%setup -n %{rname}-%{version}

cat <<EOF >gnome-%{name}.desktop
[Desktop Entry]
Name=Gv4l
Comment=%{summary}
Icon=gv4l/gv4l.png
Exec=%{name}
Terminal=false
Type=Application
EOF

%build
%configure \
	--disable-dependency-tracking \
	--with-linux="/lib/modules/2.4.20-19.9/build"
	--with-linux-include="/lib/modules/2.4.20-19.9/build/include"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
desktop-file-install --vendor gnome                \
	--add-category X-Red-Hat-Base              \
	--add-category Application                 \
	--add-category AudioVideo                  \
	--dir %{buildroot}%{_datadir}/applications \
	gnome-%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUG-REPORT-ADDRESS ChangeLog COPYING FAQ NEWS README THANKS TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop

%changelog
* Thu Jul 31 2003 Dag Wieers <dag@wieers.com> - 0.9.1-0
- Initial package. (using DAR)
