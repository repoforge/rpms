# $Id: memcached.spec 4876 2006-11-11 11:55:45Z dag $
# Authority: dag
# Upstream: Brad Fitzpatrick <brad$danga,com>

### perl-AnyEvent is rfx on EL5, and so memcached must be as well
%{?el5:# Tag: rfx}
### EL6 ships with memcached-1.4.4-3.el6
%{?el6:# Tag: rfx}

%ifarch %{ix86}
%define build_64bit --disable-64bit
%else
%define build_64bit --enable-64bit
%endif

Summary: Distributed memory object caching system
Name: memcached
Version: 1.4.14
Release: 1%{?dist}
License: BSD
Group: System Environment/Daemons
URL: http://memcached.org/

Source: http://memcached.googlecode.com/files/memcached-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: cyrus-sasl-devel
BuildRequires: libevent-devel
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig, /sbin/service
Requires(postun): /sbin/service

%description
memcached is a high-performance, distributed memory object caching system,
generic in nature, but intended for use in speeding up dynamic web
applications by alleviating database load.

%package devel
Group: Development/Tools
Summary: Header files for memcached

%description devel
Install this package if you want to develop programs that link against
memcached.

%prep
%setup

%{__cat} <<EOF >memcached.sysconfig
PORT="11211"
USER="nobody"
MAXCONN="1024"
CACHESIZE="64"
OPTIONS=""
EOF

%build
%configure \
	--program-prefix="%{?_program_prefix}" \
	--disable-dependency-tracking \
	--enable-sasl \
    %{build_64bit}
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0755 scripts/memcached.sysv %{buildroot}%{_sysconfdir}/rc.d/init.d/memcached
%{__install} -Dp -m0644 memcached.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/memcached

%{__install} -Dp -m0755 scripts/memcached-tool %{buildroot}%{_bindir}
%{__install} -Dp -m0755 scripts/mc_slab_mover %{buildroot}%{_bindir}

%{__install} -Dp -m0755 scripts/damemtop %{buildroot}%{_bindir}
%{__install} -Dp -m0644 scripts/damemtop.yaml %{buildroot}%{_sysconfdir}

%post
/sbin/chkconfig --add memcached

%preun
if [ $1 -eq 0 ]; then
	/sbin/service memcached stop &> /dev/null || :
	/sbin/chkconfig --del memcached
fi

%postun
/sbin/service memcached condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog doc/*.txt NEWS scripts/README.damemtop
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/sysconfig/memcached
%config(noreplace) %{_sysconfdir}/damemtop.yaml
%config %{_initrddir}/memcached
%{_bindir}/damemtop
%{_bindir}/memcached
%{_bindir}/memcached-tool
%{_bindir}/mc_slab_mover

%files devel
%{_includedir}/memcached

%changelog
* Wed Aug 22 2012 Steve Huff <shuff@vecna.org> - 1.4.14-1
- Updated to 1.4.14.
- Replace custom SysV init script with stock.
- Install mc_slab_mover utility.

* Thu Aug 25 2011 Steve Huff <shuff@vecna.org> - 1.4.7-1
- Updated to 1.4.7.
- Install damemtop in a sensible place.

* Fri Aug 05 2011 Steve Huff <shuff@vecna.org> - 1.4.6-1
- Updated to 1.4.6.
- Tagged as RFX in el5 as well (due to perl-AnyEvent dependency).

* Fri Apr 16 2010 Steve Huff <shuff@vecna.org> - 1.4.5-1
- Updated to 1.4.5.

* Wed Mar 31 2010 Steve Huff <shuff@vecna.org> - 1.4.4-2
- Rebuild against libevent-1.4.13 on EL5.

* Mon Feb 08 2010 Steve Huff <shuff@vecna.org> - 1.4.4-1
- Updated to 1.4.4.
- Split off include files into memcached-devel.
- Install memcached-tool in %{_bindir}, install damemtop in %{_docdir}.

* Wed Aug 20 2008 Michael Best <mbest@pendragon.org> 1.2.6
- Update to 1.2.6.

* Tue May 29 2007 Matthias Saou <http://freshrpms.net/> 1.2.2-1
- Update to 1.2.2.
- Enable new threads feature.

* Sun Mar 25 2007 Dag Wieers <dag@wieers.com> - 1.2.1-4
- Rebuild against libevent-1.1a on EL5.

* Wed Mar 07 2007 Dag Wieers <dag@wieers.com> - 1.2.1-3
- Rebuild against libevent-1.3b.

* Tue Feb 20 2007 Dag Wieers <dag@wieers.com> - 1.2.1-2
- Rebuild against libevent-1.3a.

* Mon Feb 19 2007 Dag Wieers <dag@wieers.com> - 1.2.1-1
- Updated to release 1.2.1.

* Wed Nov 01 2006 Dag Wieers <dag@wieers.com> - 1.1.13-1
- Updated to release 1.1.13.

* Sat Aug 19 2006 Dag Wieers <dag@wieers.com> - 1.1.12-3
- Rebuild against libevent-1.1b.

* Mon Apr 03 2006 Dag Wieers <dag@wieers.com> - 1.1.12-2
- Rebuild against libevent-1.1a.

* Wed Jan 11 2006 Matthias Saou <http://freshrpms.net/> 1.1.12-1
- Update to 1.1.12.
- Remove no longer needed segfault patch.
- Add Requires(foo):...
- Remove INSTALL from %%doc.
- Don't have the init script be tagged as config, the config part is all in
  the sysconfig file.
- make install now works again.
- Fix non working reload in the init script.

* Mon Mar 07 2005 Dag Wieers <dag@wieers.com> - 1.1.11-1
- Cosmetic changes.

* Thu Feb 24 2005 Rob Starkey <falcon@rasterburn.com> - 1.1.11-1
- Initial package.
