Name:           thinkfinger
Version:        0.3
Release:        2%{?dist}
Summary:        A driver for the UPEK/SGS Thomson Microelectronics fingerprint reader
Group:          System Environment/Base
License:        GPL
URL:            http://thinkfinger.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        README.thinkfinger
Patch0:         thinkfinger-0.3-birdir.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  libusb-devel >= 0.1.11
BuildRequires:  pam-devel
BuildRequires:  doxygen

%description
ThinkFinger is a driver for the UPEK/SGS Thomson Microelectronics fingerprint
reader (USB ID 0483:2016). The device is being found either as a standalone USB
device, built into USB keyboards or built into laptops.  The following laptop
vendors are using the device:

- Dell
- IBM/Lenovo
- Toshiba

Toshiba is shipping their laptops either with the UPEK/SGS Thomson
Microelectronics fingerprint reader or with a fingerprint reader built by
AuthenTec. The AuthenTec fingerprint reader is *not* supported by ThinkFinger.

SONY laptops with the UPEK/SGS Thomson Microelectronics fingerprint reader are
not supported.

%package        devel
Summary:        Development package for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       libusb-devel
Requires:       pkgconfig

%description    devel
ThinkFinger is a driver for the UPEK/SGS Thomson Microelectronics fingerprint
reader (USB ID 0483:2016). The device is being found either as a standalone USB
device, built into USB keyboards or built into laptops.  The following laptop
vendors are using the device:

- Dell
- IBM/Lenovo
- Toshiba

Toshiba is shipping their laptops either with the UPEK/SGS Thomson
Microelectronics fingerprint reader or with a fingerprint reader built by
AuthenTec. The AuthenTec fingerprint reader is *not* supported by ThinkFinger.

SONY laptops with the UPEK/SGS Thomson Microelectronics fingerprint reader are
not supported. This package contains development files for %{name}.

%prep
%setup -q
#%patch0 -p1 -b .securitydir
%{__install} -pm 644 %{SOURCE1} README.Fedora


%build
%configure --disable-static\
           --with-securedir=/%{_lib}/security
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

#kill libtool archives
rm -f $RPM_BUILD_ROOT%{_libdir}/libthinkfinger.la

#create folder where fingerprints will be stored
%{__mkdir} -p $RPM_BUILD_ROOT%{_sysconfdir}/pam_thinkfinger

#load uinput module automatically
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig/modules
cat >$RPM_BUILD_ROOT/etc/sysconfig/modules/thinkfinger.modules <<EOF
#!/bin/sh
modprobe uinput >/dev/null 2>&1
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README README.Fedora
%{_libdir}/libthinkfinger.so.*
/%{_lib}/security/pam_thinkfinger.so
%{_sbindir}/tf-tool
%{_mandir}/man1/tf-tool.1.gz
%{_mandir}/man8/pam_thinkfinger.8.gz
%{_sysconfdir}/pam_thinkfinger
%config %attr(0755,root,root)/etc/sysconfig/modules/thinkfinger.modules 

%files devel
%defattr(-,root,root,-)
%doc docs/autodocs/html/*
%{_includedir}/libthinkfinger.h
%{_libdir}/libthinkfinger.so
%{_libdir}/pkgconfig/libthinkfinger.pc



%changelog
* Fri May 18 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.3-2
- Merged Jose Plans' changes (RH #237817)

* Fri Apr 13 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.3-1
- Updated to 0.3
- Added uinput loading snippet

* Tue Feb 20 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.2.2-4
- Fixed Source0 URL

* Mon Feb 19 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.2.2-3
- Added libusb-devel to -devel subpackage Requires

* Mon Feb 19 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.2.2-2
- Fixed stripping problem properly

* Mon Feb 19 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.2.2-1
- Initial RPM release
