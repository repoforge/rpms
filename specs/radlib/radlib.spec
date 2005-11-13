# $Id$
# Authority: dries
# Upstream: Mark Teel <mark$teel,ws>

Summary: C language library for interprocess communications and common tasks
Name: radlib
Version: 2.5.0
Release: 1
License: BSD
Group: Development/Libraries
URL: http://www.radlib.teel.ws/

Source: http://dl.sf.net/radlib/radlib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
radlib is a C language library developed to abstract details of interprocess 
communications and common Linux/Unix system facilities so that application 
developers can concentrate on application solutions. It encourages 
developers to use a proven paradigm of event-driven, asynchronous design. 
By abstracting interprocess messaging, events, timers, and any I/O device 
that can be represented as a file descriptor, radlib simplifies the 
implementation of multi-purpose processes, as well as multi-process 
applications. In short, radlib is a sincere attempt to provide real-time 
OS capability on a non-real-time OS.

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
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_libdir}/librad.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/rad*.h
%{_libdir}/librad.a
%{_libdir}/librad.so
%exclude %{_libdir}/*.la

%changelog
* Fri Nov 04 2005 Dries Verachtert <dries@ulyssis.org> - 2.5.0-1
- Initial package.
