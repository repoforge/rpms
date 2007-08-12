# $Id:$
# Authority: hadams

Name:           synce
Version:        0.9.1
Release:        10
Summary:        Serial connection support for Pocket PC devices

Group:          Applications/Communications
License:        MIT
URL:            http://synce.sourceforge.net/
Source0:        http://dl.sf.net/synce/synce-libsynce-%{version}.tar.gz
Source1:        http://dl.sf.net/synce/synce-dccm-%{version}.tar.gz
Source2:        http://dl.sf.net/synce/synce-serial-%{version}.tar.gz
Source3:        http://dl.sf.net/synce/synce-rra-%{version}.tar.gz
Source4:        http://dl.sf.net/synce/synce-librapi2-%{version}.tar.gz
Source5:        http://dl.sf.net/synce/libmimedir-0.4.tar.gz
Source6:        synce.dev
Source7:        synce-README.Fedora
Patch0:         synce-rra-Makefile.patch
Patch1:         synce-rra-devel.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  automake
BuildRequires:  libtool

Requires: ppp

%description
The purpose of the SynCE project is to provide a means of
communication with a Windows CE device from a computer running Linux,
FreeBSD or a similar operating system. The SynCE project homepage is
available here: http://synce.sourceforge.net/

%package devel
Summary: Development libraries and header files for SynCE
Group: Development
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files and link libraries for SynCE
application development. SynCE provides support for communication
between a Windows CE device (PDA, smart phone) and a Linux machine.

For more details on the SynCE project, please refer to the project's
homepage at http://synce.sourceforge.net/

%prep
%setup -q -c -a 1 -a 2 -a 3 -a 4 -a 5
%patch0
%patch1

%build
# build libsynce
cd synce-libsynce-%{version}
%configure --disable-static --disable-rpath
make
SYNCEINC="$(pwd)/lib"
SYNCELIB="$(pwd)/lib/.libs"
cd ..
# build dccm
cd synce-dccm-%{version}
%configure \
    --with-libsynce-include="${SYNCEINC}" \
    --with-libsynce-lib="${SYNCELIB}" \
    --disable-static
make LDFLAGS="-L${SYNCEINC}"
cd ..
# build librapi2
cd synce-librapi2-%{version}
%configure \
    --with-libsynce-include="${SYNCEINC}" \
    --with-libsynce-lib="${SYNCELIB}" \
    --disable-static \
    --disable-rpath
make LDFLAGS="-L${SYNCEINC}"
RAPI2INC="$(pwd)/src"
RAPI2LIB="$(pwd)/src/.libs"
cd ..
# build libmimedir
cd libmimedir-0.4
CFLAGS="$RPM_OPT_FLAGS -fPIC" %configure 
make
# build shared libmimedir to work around x86_64 build error
ld --shared --whole-archive libmimedir.a -o libmimedir.so
rm libmimedir.a
MIMEDIRINC="$(pwd)"
MIMEDIRLIB="$(pwd)"
cd ..
# build rra
cd synce-rra-%{version}
./bootstrap
%configure \
    --with-libsynce-include="${SYNCEINC}" \
    --with-libsynce-lib="${SYNCELIB}" \
    --with-librapi2-include="${RAPI2INC}" \
    --with-librapi2-lib="${RAPI2LIB}" \
    --with-libmimedir-include="${MIMEDIRINC}" \
    --with-libmimedir-lib="${MIMEDIRLIB}" \
    --disable-static \
    --disable-rpath

make LDFLAGS="-L${SYNCEINC} -L${RAPI2INC} -L${MIMEDIRLIB} --shared"
cd ..
# build the serial support
cd synce-serial-%{version}
%configure
make
cd ..

%install
rm -rf $RPM_BUILD_ROOT
for module in libsynce dccm librapi2 rra serial ; do
    cd synce-${module}-%{version}
    %makeinstall
    cd ..
done

install -m 775 libmimedir-0.4/libmimedir.so $RPM_BUILD_ROOT/%{_libdir}/libmimedir.so

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

# Enable autoconnect
install -p -m 755 -D %{SOURCE6} $RPM_BUILD_ROOT/%{_sysconfdir}/udev/scripts/synce.dev
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/dev.d/ipaq/
ln -s ../../udev/scripts/synce.dev $RPM_BUILD_ROOT/%{_sysconfdir}/dev.d/ipaq/synce.dev
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/udev/rules.d/
echo 'DRIVER=="ipaq", NAME="ipaq", SYMLINK+="ttyUSB%%n"' > \
    $RPM_BUILD_ROOT/%{_sysconfdir}/udev/rules.d/50-ipaq.rules
cp %{SOURCE7} README.Fedora

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,0755)
%doc README.Fedora

#libsynce
%{_libdir}/libsynce.so.0*
%{_mandir}/man1/synce.*
#librapi2
%{_bindir}/pcp
%{_bindir}/pls
%{_bindir}/pmkdir
%{_bindir}/pmv
%{_bindir}/prm
%{_bindir}/prmdir
%{_bindir}/prun
%{_bindir}/pstatus
%{_bindir}/rapiconfig
%{_bindir}/synce-install-cab
%{_bindir}/synce-list-programs
%{_bindir}/synce-registry
%{_bindir}/synce-remove-program
%{_libdir}/librapi.so.2*
%{_mandir}/man1/pcp.*
%{_mandir}/man1/pls.*
%{_mandir}/man1/pmkdir.*
%{_mandir}/man1/pmv.*
%{_mandir}/man1/prm.*
%{_mandir}/man1/prmdir.*
%{_mandir}/man1/prun.*
%{_mandir}/man1/pstatus.*
%{_mandir}/man1/synce-install-cab.*
%{_mandir}/man1/rapiconfig.*
%{_mandir}/man1/synce-list-programs.*
%{_mandir}/man1/synce-remove-program.*
#rra
%{_bindir}/synce-matchmaker
%{_libdir}/librra.so.0*
%{_mandir}/man1/synce-matchmaker.*
#dccm
%{_bindir}/dccm
%{_bindir}/synce-sound
%{_mandir}/man1/dccm.*
%{_mandir}/man1/synce-sound.*
#serial
%{_bindir}/synce-serial-*
%{_datadir}/synce
%{_mandir}/man8/synce-serial-*
#libmimedir
%{_libdir}/libmimedir.so

#autoconnect
%{_sysconfdir}/udev/rules.d/50-ipaq.rules
%{_sysconfdir}/udev/scripts/synce.dev
%{_sysconfdir}/dev.d/ipaq/

%files devel
%defattr(-,root,root,-)
%{_includedir}/*.h
%{_libdir}/lib*.so
%{_datadir}/aclocal/*.m4

%changelog
* Sun Aug 12 2007 Heiko Adams <info@fedora-blog.de>
0.9.1-10
- rebuild for rpmforge

* Sat Nov 11 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.9.1-9
- fix udev script (#215129, #208517)

* Fri Sep 15 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.9.1-8
- FE6 rebuild

* Thu Feb 16 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.9.1-7
- Rebuild for Fedora Extras 5
- Fix cflags and build on i386

* Mon Nov 28 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.9.1-6
- move fedora readme to external file

* Mon Nov 28 2005 Aurelien Bompard <gauret[AT]free.fr> 0.9.1-5
- enable automatic connection of the device

* Tue Sep 27 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.9.1-4
- workaround for libmimedir problem an devel

* Sun Aug 21 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.9.1-3
- fix dep problem
- add missing ldconfig

* Sun Aug 21 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.9.1-2
- reenable x86_64 (#148003)
- disable static libs

* Sat Aug 20 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.9.1-1
- beautify specfile
- upgrade to new version

* Fri Apr  1 2005 Warren Togami <wtogami@redhat.com> 0.9.0-3
- ownership/perms fix (#150016 jpo)
- libmimedir-0.4

* Thu Mar 24 2005 Thorsten Leemhuis <fedora[at]leemhuis[dot]info> 0.9.0-2
- ExcludeArch: x86_64; see #148003

* Thu Aug 19 2004 Cristian Gafton <gafton@redhat.com> 0.9.0-1
- build new spec file from scratch that groups all the little modules
  together to avoid the proliferation of another half dozen single
  purpose packages...

