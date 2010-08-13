# $Id$
# Authority: dag

Summary: Utility for extracting and converting Microsoft icon and cursor files
Name: icoutils
Version: 0.29.1
Release: 1%{?dist}
License: GPLv3+
Group: Applications/Multimedia
URL: http://www.nongnu.org/icoutils/

Source: http://savannah.nongnu.org/download/icoutils/icoutils-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext
BuildRequires: libpng-devel

%description
icoutils is a set of programs for extracting and converting images in
Microsoft Windows icon and cursor files. These files usually have the
extension .ico or .cur, but they can also be embedded in executables or
libraries.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man1/*.1*
%{_bindir}/*

%changelog
* Thu Aug 12 2010 Dag Wieers <dag@wieers.com> - 0.29.1-1
- Initial package. (using DAR)
