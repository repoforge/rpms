# $Id$

# Authority: dag
# Upstream: Tomasz Maka <pasp@ll.pl>

%define rversion 0.2.2a

Summary: Graphical address book
Name: dlume
Version: 0.2.2
Release: 1.a
License: GPL
Group: Applications/Productivity
URL: http://clay.ll.pl/dlume.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://clay.ll.pl/download/dlume-%{rversion}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: gtk2-devel >= 2.2.0
BuildRequires: libxml2-devel >= 2.4.0, ImageMagick

%description
Dlume is nice, graphical address book. You can easily add, edit,
and delete records from an XML database. A Quick-search makes it
easy to find entries. Exporting to CSV and HTML formats is also
possible.

%prep
%setup -n %{name}-%{rversion}

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Dlume Address Manager
Comment=Manage contacts and addresses.
Icon=dlume.png
Exec=dlume
Terminal=false
Type=Application
Categories=GNOME;Application;Office;
EOF

%build 
%configure \
	--enable-nls
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
#%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor net                  \
        --add-category X-Red-Hat-Base              \
        --dir %{buildroot}%{_datadir}/applications \
        %{name}.desktop

%clean
%{__rm} -rf %{buildroot}

#%files -f %{name}.lang
%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png

%changelog
* Mon Mar 15 2004 Dag Wieers <dag@wieers.com> - 0.2.2-1.a
- Updated to release 0.2.2a.

* Fri Mar 12 2004 Dag Wieers <dag@wieers.com> - 0.2.0-1
- Initial package. (using DAR)
