# $Id$
# Authority: dag
# ExcludeDist: rh7 rh9

Summary: Conversion between character sets and surfaces
Name: recode
Version: 3.6
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://recode.progiciels-bpi.ca/

Source: http://recode.progiciels-bpi.ca/archives/recode-%{version}.tar.gz
Patch0: recode.patch
Patch1: recode-3.6-getcwd.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
recode converts files between character sets and usages. It recognises or
produces nearly 150 different character sets and is able to transliterate
files between almost any pair. When exact transliteration are not possible,
it may get rid of the offending characters or fall back on approximations.
Most RFC 1345 character sets are supported.

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
%patch0 -p1
%patch1 -p1 -b .getcwd

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_infodir}/dir

%post
/sbin/ldconfig
if [ -e "%{_infodir}/recode.info.gz" ]; then
	/sbin/install-info %{_infodir}/recode.info.gz %{_infodir}/dir || :
fi

%preun
if [ -e "%{_infodir}/recode.info.gz" ]; then
	/sbin/install-info --delete %{_infodir}/recode.info.gz %{_infodir}/dir || :
fi

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BACKLOG ChangeLog COPYING* NEWS README THANKS TODO
%doc %{_infodir}/recode.info*
%doc %{_mandir}/man1/recode.1*
%{_bindir}/recode
%{_libdir}/librecode.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/recode.h
%{_includedir}/recodext.h
%{_libdir}/librecode.so
%exclude %{_libdir}/librecode.la

%changelog
* Fri Jun 08 2007 Dag Wieers <dag@wieers.com> - 3.6-1
- Initial package. (using DAR)
