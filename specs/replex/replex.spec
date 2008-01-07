# $Id$
# Authority: dag
# Upstream: Marcus Metzler <mocm@metzlerbros.de>

Summary: Remultiplex transport stream (TS) data taken from a DVB source
Name: replex
Version: 0.1.6.8
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.metzlerbros.org/dvb/

Source: http://www.metzlerbros.org/dvb/replex-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Replex was created to remultiplex transport stream (TS) data taken from a DVB
source. The result is supposed to be a program stream (PS) that can be used to
be burned to a DVD (with dvdauthor).

Replex can also remultiplex other PSs and AVIs with MPEG2 content.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
export CFLAGS="%{optflags} -O6 -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -DVERSION=\\\"\$(VERSION)\\\""
export LDFLAGS="%{optflags}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -dp -m0755 %{buildroot}%{_bindir}
%{__install} -dp -m0755 %{buildroot}%{_libdir}
%{__make} install DESTDIR="%{buildroot}%{_prefix}" LIBDIR="%{buildroot}%{_libdir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr (-, root, root, 0755)
%doc CHANGES COPYING README TODO
%{_bindir}/replex

%files devel
%defattr (-, root, root, 0755)
%{_libdir}/libreplex.a

%changelog
* Sat Jan 05 2008 Dag Wieers <dag@wieers.com> - 0.1.6.8-1
- Initial package. (using DAR)
