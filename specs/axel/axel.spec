# $Id$
# Authority: dag

Summary: Light download accelerator
Name: axel
Version: 1.1
Release: 1
License: GPLv2
Group: Applications/Internet
URL: http://axel.alioth.debian.org/

Source: http://alioth.debian.org/frs/download.php/2287/axel-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, binutils

%description
Axel tries to accelerate the downloading process by using multiple
connections for one file. Starting from version 0.97, the program can use
different URL's for one download as well. The program tries to be as light
as possible (25-30k in binary form), so it might be useful as a wget clone
on byte-critical systems.

%prep
%setup

%build
./configure \
    --etcdir="%{_sysconfdir}" \
    --mandir="%{_mandir}" \
    --prefix="%{_prefix}" \
    --i18n="1"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc API CHANGES COPYING CREDITS README axelrc.example
%doc %{_mandir}/man1/axel.1*
%config %{_sysconfdir}/axelrc
%{_bindir}/axel

%changelog
* Mon Jul 28 2008 Ahmed Medhat <ultimatetux@gmail.com> - 1.1-1
- Initial RPM creation.
