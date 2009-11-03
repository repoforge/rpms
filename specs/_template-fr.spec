# $Id: _template.spec.freshrpms,v 1.2 2004/02/27 00:34:01 thias Exp $
# Authority: matthias


Summary: 
Name: 
Version: 
Release: 1%{?dist}
License: GPL
Group: 
URL: 
Source0: 
Source1: 
Patch0: 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: 
BuildRequires: 


%description


%package devel
Summary: 
Group: Development/Libraries
Requires: %{name} = %{version}, pkgconfig

%description devel


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%post
if [ $1 -eq 1 ]; then
    /sbin/chkconfig --add foobar
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/service foobar stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del foobar
fi

%postun
if [ $1 -ge 1 ]; then
    /sbin/service foobar condrestart >/dev/null 2>&1 || :
fi


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/*
%{_mandir}/man?/*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so


%changelog
* Thu Jul  1 2004 Matthias Saou <http://freshrpms.net/> 0-1
- Initial RPM release.

