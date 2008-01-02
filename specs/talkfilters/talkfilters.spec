# $Id$
# Authority: dries
# Upstream: Mark Lindner <mark_a_lindner$yahoo,com>

Summary: converts ordinary English text into text that mimics a certain dialect
Name: talkfilters
Version: 2.3.8
Release: 1
License: GPL
Group: Amusements/Games
URL: http://www.hyperrealm.com/main.php?s=talkfilters

Source: http://www.hyperrealm.com/talkfilters/talkfilters-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: 

%description
The GNU Talk Filters are filter programs that convert ordinary English text 
into text that mimics a stereotyped or otherwise humorous dialect. These 
filters have been in the public domain for many years, but now for the first 
time they are provided as a single integrated package. The filters include 
austro, b1ff, brooklyn, chef, cockney, drawl, dubya, fudd, funetak, jethro, 
jive, kraut, pansy, pirate, postmodern, redneck, valspeak, and warez. Each 
program reads from standard input and writes to standard output. The package 
also provides the filters as a C library, so they can be easily used by other 
programs.

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
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/talkfilters.1*
%doc %{_mandir}/man1/wrap.1*
%{_bindir}/austro
%{_bindir}/b1ff
%{_bindir}/brooklyn
%{_bindir}/chef
%{_bindir}/cockney
%{_bindir}/drawl
%{_bindir}/dubya
%{_bindir}/fudd
%{_bindir}/funetak
%{_bindir}/jethro
%{_bindir}/jive
%{_bindir}/kraut
%{_bindir}/pansy
%{_bindir}/pirate
%{_bindir}/postmodern
%{_bindir}/redneck
%{_bindir}/valspeak
%{_bindir}/warez
%{_bindir}/wrap
%{_libdir}/libtalkfilters.so.*
%{_infodir}/talkfilters.info*
%exclude %{_libdir}/libtalkfilters.a
%exclude %{_libdir}/libtalkfilters.la

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/talkfilters.h
%{_libdir}/libtalkfilters.so
%{_libdir}/pkgconfig/talkfilters.pc

%changelog
* Wed Jan  2 2008 Dries Verachtert <dries@ulyssis.org> - 2.3.8-1
- Initial package.
