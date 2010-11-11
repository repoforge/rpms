# $Id$
# Authority: dag
# Upstream: Markus F.X.J. Oberhumer <markus$oberhumer,com>

### EL6 ships with lzop-1.02-0.9.rc1.el6
# ExclusiveDist: el2 el3 el4 el5

Summary: Real-time file compressor
Name: lzop
Version: 1.03
Release: 1%{?dist}
License: GPL
Group: Applications/Archiving
URL: http://www.lzop.org/

Source: http://www.lzop.org/download/lzop-%{version}.tar.gz
Patch0: lzop-1.01-gcc29.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: lzo-devel

%description
lzop is a compression utility which is designed to be a companion to gzip. It
is based on the LZO library and its main advantages over gzip are much higher
compression and decompression speed at the cost of compression ratio.

lzop was designed with reliability, speed and portability in mind and as a
reasonable drop-in compatiblity to gzip.

%prep
%setup
%patch0

%build
%configure \
    --program-prefix="%{?_program_prefix}"
echo "#define _LARGE_FILES 1" >>config.h
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS NEWS README THANKS
%doc %{_mandir}/man1/lzop.1*
%{_bindir}/lzop

%changelog
* Wed Nov 10 2010 Dag Wieers <dag@wieers.com> - 1.03-1
- Updated to release 1.03.

* Fri Mar 02 2007 Dag Wieers <dag@wieers.com> - 1.01-2
- Fix large file support. (Joe Buehler)

* Tue Mar 09 2004 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
