# $Id$

# Authority: dag

### FIXME: Makefiles don't allow -jX (parallel compilation)
# Distcc: 0

### FIXME: TODO: Add desktop file.

%define rversion 040301

Summary: PostScript font editor
Name: pfaedit
Version: 0.0.20040301
Release: 0
License: BSD
Group: Applications/Publishing
URL: http://pfaedit.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/pfaedit/pfaedit_full-%{rversion}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: libpng-devel, libungif-devel, libtiff-devel, libjpeg-devel, libuninameslist-devel

%description
PfaEdit allows you to edit outline and bitmap fonts.  You can create
new ones or modify old ones.  It is also a font format converter and
can convert among PostScript (ASCII & binary Type 1, some Type 3s,
some Type 0s), TrueType, OpenType (Type2) and CID-keyed fonts.

%prep
%setup -T -b0 -n %{name}-%{rversion}

%build
%configure \
	--disable-shared
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
#{__make} install \
#	libdir="%{buildroot}%{_libdir}" \
#	bindir="%{buildroot}%{_bindir}" \
#	mandir="%{buildroot}%{_mandir}"

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.{a,la}
#{__rm} -rf %{buildroot}%{_libdir}/debug/

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING LICENSE README
%doc %{_mandir}/man?/*
%{_bindir}/*
#{_libdir}/*.so.*
%{_datadir}/pfaedit/

%changelog
* Sat Mar 06 2004 Dag Wieers <dag@wieers.com> - 0.0.20040301-0
- Updated to release 040301.

* Mon Jul 28 2003 Dag Wieers <dag@wieers.com> - 0.0.20030720-0
- Initial package. (using DAR)
