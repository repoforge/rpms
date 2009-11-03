# $Id$

# Authority: dries

Summary: Objective Caml interface to gtk+
Name: lablgtk
Version: 2.4.0
Release: 1.2%{?dist}
License: GPL
Group: Development/Libraries
URL: http://wwwfun.kurims.kyoto-u.ac.jp/soft/olabl/lablgtk.html

Source: http://wwwfun.kurims.kyoto-u.ac.jp/soft/olabl/dist/lablgtk-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ocaml, pkgconfig, gtk2-devel, libglade2-devel
BuildRequires: librsvg2-devel, libgnomecanvas-devel, libgnomeui-devel
BuildRequires: gnome-panel-devel

%description
LablGTK is is an Objective Caml interface to gtk+.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags} world all opt

%install
%{__rm} -rf %{buildroot}
%makeinstall INSTALLDIR=%{buildroot}%{_libdir}/ocaml/lablgtk2 DLLDIR=%{buildroot}%{_libdir}/ocaml/stublibs LIBDIR=%{buidlroot}%{_libdir}/ocaml BINDIR=%{buildroot}%{_bindir}

%{__install} -d %{buildroot}%{_libdir}/ocaml/site-lib/labl{gtk2,gnomecanvas,glade,gtkgl,rsvg}
cat > %{buildroot}%{_libdir}/ocaml/site-lib/lablgtk2/META <<EOF
requires = ""
version = "%{version}"
directory = "+lablgtk2"
archive(byte) = "lablgtk.cma gtkInit.cmo"
archive(native) = "lablgtk.cmxa gtkInit.cmx"
linkopts = ""
EOF

for i in gnomecanvas glade gtkgl rsvg ; do
cat > %{buildroot}%{_libdir}/ocaml/site-lib/labl${i}/META <<EOF
requires = "lablgtk"
version = "%{version}"
directory = "+lablgtk"
archive(byte) = "labl${i}.cma"
archive(native) = "labl${i}.cmxa"
linkopts = ""
EOF
done

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README
%{_libdir}/ocaml/stublibs/dlllabl*
%{_libdir}/ocaml/lablgtk2
%{_bindir}/lablgtk2
%{_bindir}/lablgladecc2
%{_libdir}/ocaml/site-lib/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.4.0-1.2
- Rebuild for Fedora Core 5.

* Thu Dec 09 2004 Dries Verachtert <dries@ulyssis.org> - 2.4.0-1
- Initial package.
  The shellcode which creates the meta information is based on the spec file
  made by the PLD Team ( http://www.pld.org.pl/ ).
