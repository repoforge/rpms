# $Id$

# Authority: dag

Summary: GUI editor for creating man pages. 
Name: manedit
Version: 0.5.10
Release: 0
License: GPL
Group: Development/Tools
URL: http://wolfpack.twu.net/ManEdit/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://wolfpack.twu.net/users/wolfpack/manedit-0.5.10.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: gtk+-devel, zlib-devel
Requires: groff

%description
ManEdit is a UNIX Manual Page Integrated Development Environment.
It has full UNIX manual page editing capabilities using an XML
interface with instant preview. ManEdit uses the GTK+ widget set
and requires the X Window Systems.

%prep
%setup

%{__perl} -pi.orig -e 's|/usr/man|%{_mandir}|' manedit/pref.c manedit/prefcb.c

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Manpage Editor
Comment=%{summary}
Exec=%{name}
Icon=/usr/share/icons/manedit.xpm
Terminal=false
Type=Application
Categories=Application;Development;
EOF

%build
./configure Linux \
	--prefix="%{_prefix}" \
	--mandir="%{_mandir}" \
	--disable="arch-i486" \
	--disable="arch-i586" \
	--disable="arch-i686" \
	--disable="arch-pentiumpro"
%{__make} %{?_smp_mflags} 

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	PREFIX="%{buildroot}%{_prefix}" \
	MAN_DIR="%{buildroot}%{_mandir}/man1"

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor net                  \
	--add-category X-Red-Hat-Base                \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0755)
%doc AUTHORS LICENSE  README 
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/manedit/
%{_datadir}/icons/*
%{_datadir}/applications/*.desktop
 
%changelog
* Sun Oct 05 2003 Dag Wieers <dag@wieers.com> - 0.5.10-0
- Initial package. (using DAR)
