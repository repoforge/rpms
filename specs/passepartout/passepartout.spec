# Authority: dag

# Upstream: Fredrik Arnerup <e97_far@e.kth.se>

Summary: Open Source desktop publishing application.
Name: passepartout
Version: 0.4
Release: 0
License: BSD
Group: Applications/Multimedia
URL: http://www.stacken.kth.se/project/pptout/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.stacken.kth.se/project/pptout/files/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: libxml++ >= 1.0, gtkmm2

%description
Passepartout is an Open Source Desktop Publishing application for the
X Windows environment. The goal of this project is to create a system
capable of producing pre-press material of professional quality, but
also a useful tool for any enthusiast with access to a printer.

The main focus is on making it easy for the user to create publications
with a flexible layout, typical examples being magazines, brochures and
leaflets.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Passepartout Desktop Publishing
Comment=%{summary}
Icon=redhat-presentations.png
Exec=passepartout
Terminal=false
Type=Application
Categories=GNOME;Application;Graphics;
EOF

%build
%configure \
	--disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_docdir}/passepartout/*.xslt \
		%{buildroot}%{_docdir}/passepartout/examples/*.xslt

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor gnome                \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS COPYING NEWS README
%doc %{_mandir}/man?/*
%doc %{_docdir}/passepartout/
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/xml/passepartout/

%changelog
* Thu Jan 15 2004 Dag Wieers <dag@wieers.com> - 0.4-0
- Updated to release 0.4.

* Mon Jan 05 2004 Dag Wieers <dag@wieers.com> - 0.3-1
- Fixed desktop-file to start passepartout. (Peter Robertson)

* Thu Nov 20 2003 Dag Wieers <dag@wieers.com> - 0.3-0
- Updated to release 0.3.

* Thu Sep 11 2003 Dag Wieers <dag@wieers.com> - 0.2-0
- Initial package. (using DAR)
