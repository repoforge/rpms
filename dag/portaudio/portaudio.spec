# Authority: atrpms
%define rversion v18_1

Summary: A free, cross platform, open-source, audio I/O library.
Name: portaudio
Version: 18.1
Release: 0
License: distributable
Group: System Environment/Libraries
URL: http://www.portaudio.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.portaudio.com/archives/%{name}_%{rversion}.zip
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
PortAudio is a portable audio I/O library designed for cross-platform
support of audio. It uses a callback mechanism to request audio processing.
Audio can be generated in various formats, including 32 bit floating point,
and will be converted to the native format internally.

%prep
%setup -n %{name}_%{rversion} 

%{__perl} -pi.orig -e 's|^(LIBINST =) /usr/local/lib|$1 %{_libdir}|' Makefile.linux

%build
%{__make} %{?_smp_mflags} -f Makefile.linux sharedlib
#%{__make} %{?_smp_mflags} -C pa_unix_oss

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_libdir} \
			%{buildroot}%{_includedir}
#%{__install} -m0755 pa_unix_oss/patest %{buildroot}%{_bindir}
%{__install} -m0755 pa_unix_oss/libportaudio.so %{buildroot}%{_libdir}
%{__install} -m0644 pa_common/portaudio.h %{buildroot}%{_includedir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644, root, root, 0755)
%doc LICENSE.txt README.txt docs/
#%{_bindir}/patest
%{_libdir}/*.so
%{_includedir}/*.h

%changelog
* Sat Sep 13 2003 Dag Wieers <dag@wieers.com> - 18.1-0
- Initial package. (using DAR)
