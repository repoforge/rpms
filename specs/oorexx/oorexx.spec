# $Id$
# Authority: dag

%define real_name ooRexx

Summary: Open Object Rexx
Name: oorexx
Version: 3.0.0
Release: 1
License: CPL
Group: Development/Languages
URL: http://www.oorexx.org/

Source: http://dl.sf.net/oorexx/ooRexx-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes: ooRexx <= %{version}

%description
Open Object Rexx is an object-oriented scripting language. The language
is designed for "non-programmer" type users, so it is easy to learn
and easy to use, and provides an excellent vehicle to enter the world
of object-oriented programming without much effort.

It extends the procedural way of programming with object-oriented
features that allow you to gradually change your programming style
as you learn more about objects.

%prep
%setup -n %{real_name}-%{version}

#%ifarch x86_64
#%{__perl} -pi.orig -e 's|-m32|-m64|g;' configure
#%endif
%{__perl} -pi.orig -e 's|-m32||g;' configure

%build
%configure \
	--disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Fix library symlinks
for lib in $(ls %{buildroot}%{_libdir}/ooRexx/*.so.?.?.?); do
	%{__ln_s} -f $(basename $lib) ${lib//%\.?}
	%{__ln_s} -f $(basename $lib) ${lib//%\.?\.?}
	%{__ln_s} -f $(basename $lib) ${lib//%\.?\.?\.?}
done

%files
%defattr(-, root, root, 0755)
%doc CPLv1.0.txt INSTALL samples/
%doc %{_mandir}/man1/rexx*.1*
%doc %{_mandir}/man1/rx*.1*
%{_bindir}/rexx*
%{_bindir}/rx*
%{_datadir}/ooRexx/
%{_includedir}/rexx.h
%{_libdir}/ooRexx/

%changelog
* Mon Mar 28 2005 Dag Wieers <dag@wieers.com> - 3.0.0-1
- Initial package. (using DAR)
