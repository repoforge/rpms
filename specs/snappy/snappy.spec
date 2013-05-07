Name:           snappy
Version:        1.1.0
Release:        1%{?dist}
Summary:        Fast compression and decompression library

Group:          System Environment/Libraries
License:        BSD
URL:            http://code.google.com/p/snappy/
Source0:        http://snappy.googlecode.com/files/%{name}-%{version}.tar.gz

#BuildRequires:  gtest-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Snappy is a compression/decompression library. It does not aim for maximum 
compression, or compatibility with any other compression library; instead, it 
aims for very high speeds and reasonable compression. For instance, compared to 
the fastest mode of zlib, Snappy is an order of magnitude faster for most 
inputs, but the resulting compressed files are anywhere from 20% to 100% 
bigger. 


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure CXXFLAGS="%{optflags} -DNDEBUG" --disable-static
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_datadir}/doc/snappy/
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%clean
rm -rf %{buildroot}

%check
make check


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/libsnappy.so.*

%files devel
%defattr(-,root,root,-)
%doc format_description.txt
%{_includedir}/snappy*.h
%{_libdir}/libsnappy.so


%changelog
* Tue May 07 2013 David Hrbáč <david@hrbac.cz> - 1.1.0-1
- new upstream release

* Mon Feb 27 2012 David Hrbáč <david@hrbac.cz> - 1.0.5-1
- new upstream release

* Mon Feb 13 2012 David Hrbáč <david@hrbac.cz> - 1.0.4-1
- initial release
