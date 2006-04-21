# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%{?rh7:%define _without_python2 1}
%{?el2:%define _without_python2 1}

Summary: Tool to access devices via the OBEX protocol
Name: obexftp
Version: 0.18
Release: 1.2
License: GPL
Group: Applications/Communication
URL: http://openobex.triq.net/

#Source: http://dl.sf.net/openobex/obexftp-%{version}.tar.gz
Source: http://triq.net/obexftp/obexftp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openobex-devel, bluez-libs-devel

%description
The overall goal of this project is to make mobile devices featuring the OBEX
protocol and adhering to the OBEX FTP standard accessible by an open source
implementation. The common usage for ObexFTP is to access your mobile phones
memory to store and retrieve e.g. your phonebook, logos, ringtones, music,
pictures and alike

%package -n libobexftp
Summary: Library to access devices via the OBEX protocol
Group: System Environment/Libraries

%description -n libobexftp
The overall goal of this project is to make mobile devices featuring the OBEX
protocol and adhering to the OBEX FTP standard accessible by an open source
implementation. The common usage for ObexFTP is to access your mobile phones
memory to store and retrieve e.g. your phonebook, logos, ringtones, music,
pictures and alike

%package -n libobexftp-devel
Summary: Header files, libraries and development documentation for libobexftp.
Group: Development/Libraries
Requires: libobexftp = %{version}-%{release}

%description -n libobexftp-devel
This package contains the header files, static libraries and development
documentation for libobexftp. If you like to develop programs using libobexftp,
you will need to install libobexftp-devel.

%package -n python-obexftp
Summary: Library to access devices via the OBEX protocol
Group: Development/Libraries
Requires: libobexftp = %{version}-%{release}

%description -n python-obexftp
The overall goal of this project is to make mobile devices featuring the OBEX
protocol and adhering to the OBEX FTP standard accessible by an open source
implementation. The common usage for ObexFTP is to access your mobile phones
memory to store and retrieve e.g. your phonebook, logos, ringtones, music,
pictures and alike

%prep
%setup

%build
### FIXME: Disabled perl because cannot make Makefile place it in DESTDIR
%configure \
	%{?_without_python2:--disable-python} \
	--disable-perl \
	--disable-tcl
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%post -n libobexftp -p /sbin/ldconfig
%postun -n libobexftp -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README* THANKS TODO
%doc %{_mandir}/man1/obexftp.1*
%{_bindir}/obexftp

%files -n libobexftp
%defattr(-, root, root, 0755)
%{_libdir}/*.so.*

%files -n libobexftp-devel
%defattr(-, root, root, 0755)
%{_includedir}/bfb/
%{_includedir}/multicobex/
%{_includedir}/obexftp/
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so

%if %{!?_without_python2:1}0
%files -n python-obexftp
%defattr(-, root, root, 0755)
%{python_sitearch}/obexftp/
%exclude %{python_sitearch}/obexftp/*.a
%exclude %{python_sitearch}/obexftp/*.la
%exclude %{python_sitearch}/obexftp/*.so.*
%endif

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.18-1.2
- Rebuild for Fedora Core 5.

* Sun Jan 29 2006 Dag Wieers <dag@wieers.com> - 0.18-1
- Initial package. (using DAR)
