# Authority: dag

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

%define rversion 0.2.3c

Summary: Wireless LAN (WLAN) tool which recovers encryption keys.
Name: airsnort
Version: 0.2.3
Release: 0.c
License: GPL
Group: System Environment/Base
URL: http://airsnort.shmoo.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://prdownloads.sourceforge.net/airsnort/%{name}-%{rversion}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: gtk+-devel, libgnomeui-devel >= 2.0.0

%description
AirSnort is a wireless LAN (WLAN) tool which recovers encryption keys.
AirSnort operates by passively monitoring transmissions, computing the
encryption key when enough packets have been gathered.

%prep
%setup -n %{name}-%{rversion}

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Airsnort Wireless Sniffer
Comment=Recover wireless encryption keys.
Icon=redhat-internet.png
Exec=airsnort
Terminal=false
Type=Application
Categories=GNOME;Application;Network;
EOF

%build
./autogen.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/
%{__install} -m0644 man/*.1 %{buildroot}%{_mandir}/man1/

%if %{dfi}
        %{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Network/
        %{__install} -m0644 %{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Network/
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
        desktop-file-install --vendor gnome                \
                --add-category X-Red-Hat-Base              \
                --dir %{buildroot}%{_datadir}/applications \
                %{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog LICENSE README* TODO *.txt
%doc %{_mandir}/man?/*
%{_bindir}/*
%if %{dfi}
        %{_datadir}/gnome/apps/Network/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Sat Jan 03 2004 Dag Wieers <dag@wieers.com> - 0.2.3-0.c
- Added desktop-file.
- Updated to release 0.2.3c.

* Sat Jul 12 2003 Dag Wieers <dag@wieers.com> - 0.2.2-0
- Initial package. (using DAR)
