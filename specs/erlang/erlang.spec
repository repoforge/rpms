# $Id$
# Authority: shuff
# ExcludeDist: el3

%define rel 5

Name: erlang
Version: R12B
Release: %{rel}.12%{?dist}
Summary: General-purpose programming language and runtime environment
License: ERPL
Group: Development/Languages
URL: http://www.erlang.org

Source: http://www.erlang.org/download/otp_src_%{version}-%{rel}.tar.gz
Source1: http://www.erlang.org/download/otp_doc_html_%{version}-%{rel}.tar.gz
Source2: http://www.erlang.org/download/otp_doc_man_%{version}-%{rel}.tar.gz
Patch1: otp-R12B-5-0001-Do-not-create-links-instead-of-real-files.patch
Patch2: otp-R12B-5-0002-Fix-symlinking-of-epmd.patch
Patch3: otp-R12B-5-0003-Do-not-format-man-pages.patch
Patch4: otp-R12B-5-0004-Remove-rpath.patch
Patch5: otp-R12B-5-0005-Fix-missing-ssl-libraries-in-EPEL.patch
Patch6: otp-R12B-5-0006-Fix-shared-libraries-installation.patch
Patch7: otp-R12B-5-0007-Fix-check-for-compile-workspace-overflow.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: java-1.4.2-gcj-compat-devel
BuildRequires: flex
BuildRequires: gd-devel
BuildRequires: m4
BuildRequires: ncurses-devel
BuildRequires: openssl-devel
BuildRequires: tcl-devel
BuildRequires: tk-devel
BuildRequires: unixODBC-devel

Requires:	tk

# Added virtual Provides for each erlang module
Provides: erlang-appmon = %{version}-%{release}
Provides: erlang-asn1 = %{version}-%{release}
Provides: erlang-common_test = %{version}-%{release}
Provides: erlang-compiler = %{version}-%{release}
Provides: erlang-cosEvent = %{version}-%{release}
Provides: erlang-cosEventDomain = %{version}-%{release}
Provides: erlang-cosFileTransfer = %{version}-%{release}
Provides: erlang-cosNotification = %{version}-%{release}
Provides: erlang-cosProperty = %{version}-%{release}
Provides: erlang-cosTime = %{version}-%{release}
Provides: erlang-cosTransactions = %{version}-%{release}
Provides: erlang-crypto = %{version}-%{release}
Provides: erlang-debugger = %{version}-%{release}
Provides: erlang-dialyzer = %{version}-%{release}
Provides: erlang-docbuilder = %{version}-%{release}
Provides: erlang-edoc = %{version}-%{release}
Provides: erlang-erts = %{version}-%{release}
Provides: erlang-et = %{version}-%{release}
Provides: erlang-eunit = %{version}-%{release}
Provides: erlang-gs = %{version}-%{release}
Provides: erlang-hipe = %{version}-%{release}
Provides: erlang-ic = %{version}-%{release}
Provides: erlang-inets = %{version}-%{release}
Provides: erlang-inviso = %{version}-%{release}
Provides: erlang-kernel = %{version}-%{release}
Provides: erlang-megaco = %{version}-%{release}
Provides: erlang-mnesia = %{version}-%{release}
Provides: erlang-observer = %{version}-%{release}
Provides: erlang-odbc = %{version}-%{release}
Provides: erlang-orber = %{version}-%{release}
Provides: erlang-os_mon = %{version}-%{release}
Provides: erlang-otp_mibs = %{version}-%{release}
Provides: erlang-parsetools = %{version}-%{release}
Provides: erlang-percept = %{version}-%{release}
Provides: erlang-pman = %{version}-%{release}
Provides: erlang-public_key = %{version}-%{release}
Provides: erlang-runtime_tools = %{version}-%{release}
Provides: erlang-sasl = %{version}-%{release}
Provides: erlang-snmp = %{version}-%{release}
Provides: erlang-ssh = %{version}-%{release}
Provides: erlang-ssl = %{version}-%{release}
Provides: erlang-stdlib = %{version}-%{release}
Provides: erlang-syntax_tools = %{version}-%{release}
Provides: erlang-test_server = %{version}-%{release}
Provides: erlang-toolbar = %{version}-%{release}
Provides: erlang-tools = %{version}-%{release}
Provides: erlang-tv = %{version}-%{release}
Provides: erlang-typer = %{version}-%{release}
Provides: erlang-webtool = %{version}-%{release}
Provides: erlang-xmerl = %{version}-%{release}

%description
Erlang is a general-purpose programming language and runtime
environment. Erlang has built-in support for concurrency, distribution
and fault tolerance. Erlang is used in several large telecommunication
systems from Ericsson.


%package doc
Summary: Erlang documentation
Group: Development/Languages

%description doc
Documentation for Erlang.


%prep
%setup -q -n otp_src_%{version}-%{rel}
%patch1 -p1 -b .links
%patch2 -p1 -b .fix_epmd_symlink
%patch3 -p1 -b .manpages
%patch4 -p1 -b .rpath_removal
%patch5 -p1 -b .missing_ssl_libraries
%patch6 -p1 -b .so_lib_install_fix
%patch7 -p1 -b .pcre_buffer_overflow


# enable dynamic linking for ssl
sed -i 's|SSL_DYNAMIC_ONLY=no|SSL_DYNAMIC_ONLY=yes|' erts/configure
sed -i 's|^LD.*=.*|LD = gcc -shared|' lib/common_test/c_src/Makefile
# fix for newer glibc version
sed -i 's|__GLIBC_MINOR__ <= 7|__GLIBC_MINOR__ <= 8|' erts/emulator/hipe/hipe_x86_signal.c
# use gcc -shared instead of ld
sed -i 's|@RX_LD@|gcc -shared|' lib/common_test/c_src/Makefile.in
sed -i 's|@RX_LDFLAGS@||' lib/common_test/c_src/Makefile.in


%build
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" %configure \
    --enable-dynamic-ssl-lib \
    --enable-threads \
    --enable-smp-support \
    --enable-kernel-poll \
    --enable-hipe \
    --disable-erlang-mandir 
%{__chmod} -R u+w .
%{__make}


%install
rm -rf %{buildroot}
%{__make} INSTALL_PREFIX=%{buildroot} install

# clean up
find %{buildroot}%{_libdir}/erlang -perm 0775 | xargs chmod 755
find %{buildroot}%{_libdir}/erlang -name Makefile | xargs chmod 644
find %{buildroot}%{_libdir}/erlang -name \*.o | xargs chmod 644
find %{buildroot}%{_libdir}/erlang -name \*.bat | xargs rm -f
find %{buildroot}%{_libdir}/erlang -name index.txt.old | xargs rm -f

# doc
%{__mkdir_p} erlang_doc
%{__tar} -C erlang_doc -zxf %{SOURCE1}
%{__mkdir_p} %{buildroot}%{_mandir}
%{__tar} -C %{buildroot}/%{_mandir}/.. -zxf %{SOURCE2}
# clean up some unnecessary files from the man tarball
%{__rm} -f %{buildroot}/%{_datadir}/COPYRIGHT
%{__rm} -f %{buildroot}/%{_datadir}/PR.template
%{__rm} -f %{buildroot}/%{_datadir}/README

# make links to binaries
%{__mkdir_p} %{buildroot}/%{_bindir}
cd %{buildroot}/%{_bindir}
for file in erl erlc escript dialyzer
do
  %{__ln_s} -f ../%{_lib}/erlang/bin/$file .
done

# remove buildroot from installed files
cd %{buildroot}/%{_libdir}/erlang
sed -i "s|%{buildroot}||" erts*/bin/{erl,start} releases/RELEASES bin/{erl,start}

# move aside some conflicting man pages
%{__mv} %{buildroot}%{_mandir}/man3/inet.3 %{buildroot}%{_mandir}/man3/erlang_inet.3 
%{__mv} %{buildroot}%{_mandir}/man3/queue.3 %{buildroot}%{_mandir}/man3/erlang_queue.3 
%{__mv} %{buildroot}%{_mandir}/man3/random.3 %{buildroot}%{_mandir}/man3/erlang_random.3 
%{__mv} %{buildroot}%{_mandir}/man3/rpc.3 %{buildroot}%{_mandir}/man3/erlang_rpc.3 
%{__mv} %{buildroot}%{_mandir}/man3/string.3 %{buildroot}%{_mandir}/man3/erlang_string.3 
%{__mv} %{buildroot}%{_mandir}/man3/zlib.3 %{buildroot}%{_mandir}/man3/erlang_zlib.3 

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc AUTHORS EPLICENCE README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/erlang


%files doc
%defattr(-,root,root)
%doc erlang_doc/*


%post
%{_libdir}/erlang/Install -minimal %{_libdir}/erlang >/dev/null 2>/dev/null


%changelog
* Thu Jul 01 2010 Steve Huff <shuff@vecna.org> - R12B-5.12
- A few man pages conflict with distro files; renamed them.

* Fri Jun 25 2010 Steve Huff <shuff@vecna.org> - R12B-5.11
- Ported from EPEL.
- Turned on some additional compile-time options.
- Moved man pages into standard $MANPATH.

* Mon Jun  7 2010 Peter Lemenkov <lemenkov@gmail.com> - R12B-5.10
- Added missing virtual provides erlang-erts

* Tue May 25 2010 Peter Lemenkov <lemenkov@gmail.com> - R12B-5.9
- Use java-1.4.2 only for EL-[45]
- Added virtual provides for each erlang module
- Small typo fix

* Mon Apr 19 2010 Peter Lemenkov <lemenkov@gmail.com> - R12B-5.8
- Patches rebased
- Added patches 6,7 from trunk
- Use %%configure

* Tue Apr 21 2009 Debarshi Ray <rishi@fedoraproject.org> R12B-5.7
- Updated rpath patch.
- Fixed configure to respect $RPM_OPT_FLAGS.

* Sun Mar  1 2009 Gerard Milmeister <gemi@bluewin.ch> - R12B-5.6
- new release R12B-5
- link escript and dialyzer to %{_bindir}

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - R12B-5.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 14 2009 Dennis Gilmore <dennis@ausil.us> - R12B-4.5
- fix sparc arches to compile

* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> - R12B-4.4
- rebuild with new openssl

* Sat Oct 25 2008 Gerard Milmeister <gemi@bluewin.ch> - R12B-4.1
- new release R12B-4

* Fri Sep  5 2008 Gerard Milmeister <gemi@bluewin.ch> - R12B-3.3
- fixed sslrpath patch

* Thu Jul 17 2008 Tom "spot" Callaway <tcallawa@redhat.com> - R12B-3.2
- fix license tag

* Sun Jul  6 2008 Gerard Milmeister <gemi@bluewin.ch> - R12B-3.1
- new release R12B-3

* Thu Mar 27 2008 Gerard Milmeister <gemi@bluewin.ch> - R12B-1.1
- new release R12B-1

* Sat Feb 23 2008 Gerard Milmeister <gemi@bluewin.ch> - R12B-0.3
- disable strict aliasing optimization

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - R12B-0.2
- Autorebuild for GCC 4.3

* Sat Dec  8 2007 Gerard Milmeister <gemi@bluewin.ch> - R12B-0.1
- new release R12B-0

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - R11B-6
 - Rebuild for deps

* Sun Aug 19 2007 Gerard Milmeister <gemi@bluewin.ch> - R11B-5.3
- fix some permissions

* Sat Aug 18 2007 Gerard Milmeister <gemi@bluewin.ch> - R11B-5.2
- enable dynamic linking for ssl

* Sat Aug 18 2007 Gerard Milmeister <gemi@bluewin.ch> - R11B-5.1
- new release R11B-5

* Sat Mar 24 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - R11B-2.4
- Require java-1.5.0-gcj-devel for build.

* Sun Dec 31 2006 Gerard Milmeister <gemi@bluewin.ch> - R11B-2.3
- remove buildroot from installed files

* Sat Dec 30 2006 Gerard Milmeister <gemi@bluewin.ch> - R11B-2.2
- added patch for compiling with glibc 2.5

* Sat Dec 30 2006 Gerard Milmeister <gemi@bluewin.ch> - R11B-2.1
- new version R11B-2

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - R11B-0.3
- Rebuild for FE6

* Wed Jul  5 2006 Gerard Milmeister <gemi@bluewin.ch> - R11B-0.2
- add BR m4

* Thu May 18 2006 Gerard Milmeister <gemi@bluewin.ch> - R11B-0.1
- new version R11B-0

* Wed May  3 2006 Gerard Milmeister <gemi@bluewin.ch> - R10B-10.3
- added patch for run_erl by Knut-Håvard Aksnes

* Mon Mar 13 2006 Gerard Milmeister <gemi@bluewin.ch> - R10B-10.1
- new version R10B-10

* Thu Dec 29 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-9.1
- New Version R10B-9

* Sat Oct 29 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-8.2
- updated rpath patch

* Sat Oct 29 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-8.1
- New Version R10B-8

* Sat Oct  1 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-6.4
- Added tk-devel and tcl-devel to buildreq
- Added tk to req

* Tue Sep  6 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-6.3
- Remove perl BuildRequires

* Tue Aug 30 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-6.2
- change /usr/lib to %%{_libdir}
- redirect output in %%post to /dev/null
- add unixODBC-devel to BuildRequires
- split doc off to erlang-doc package

* Sat Jun 25 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-6.1
- New Version R10B-6

* Sun Feb 13 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-3.1
- New Version R10B-3

* Mon Dec 27 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:R10B-2-0.fdr.1
- New Version R10B-2

* Wed Oct  6 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:R10B-0.fdr.1
- New Version R10B

* Thu Oct 16 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:R9B-1.fdr.1
- First Fedora release
