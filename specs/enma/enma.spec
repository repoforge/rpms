Summary: A milter program for domain authentication technologies
Name: enma
Version: 1.2.0
Release: 1
License: BSD
URL: http://enma.sourceforge.net/
Group: Applications/Internet
Source0: enma-1.2.0.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: ldns-devel >= 1.6.0
BuildRequires: sendmail-devel
BuildRequires: openssl-devel >= 0.9.8
Requires: ldns >= 1.6.0
Requires: openssl >= 0.9.8
Requires(post): chkconfig
Requires(preun): chkconfig

%description
ENMA is a program of domain authentication technologies. It authenticates
message senders with SPF, Sender ID, DKIM and/or DKIM ADSP and inserts
the Authentication-Results: field with authentication results.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_initrddir}
install -m 755 enma/etc/rc.enma-centos %{buildroot}%{_initrddir}/enma
install -m 644 enma/etc/enma.conf.sample %{buildroot}%{_sysconfdir}/enma.conf

mkdir -p %{buildroot}%{_localstatedir}/run/enma/

%clean
rm -rf %{buildroot}

%post
/sbin/chkconfig --add enma

%preun
if [ $1 = 0 ] ; then
    /sbin/service enma stop > /dev/null 2>&1
    /sbin/chkconfig --del enma
fi

%postun
if [ $1 -ge 1 ] ; then
    /sbin/service enma condrestart > /dev/null 2>&1
fi

%files
%defattr(-, root, root, -)
%doc ChangeLog LICENSE LICENSE.ja README README.ja INSTALL INSTALL.ja
%{_bindir}/*
%{_libdir}/*
%{_libexecdir}/*
%{_mandir}/*/*
%{_mandir}/ja*/*/*
%{_initrddir}/enma
%config %{_sysconfdir}/enma.conf
%attr(0750, daemon, daemon) %dir %{_localstatedir}/run/enma/

%changelog
* Tue Jan 31 2012 SUZUKI Takahiko <takahiko@iij.ad.jp>
- (1.2.0-1)
- new upstream release

* Wed Nov 30 2011 SUZUKI Takahiko <takahiko@iij.ad.jp>
- (1.1.992-1)
- new upstream release

* Mon Nov 28 2011 SUZUKI Takahiko <takahiko@iij.ad.jp>
- (1.1.991-1)
- new upstream release

* Fri Apr 03 2009 SUZUKI Takahiko <takahiko@iij.ad.jp>
- (1.1.0-1)
- new upstream release

* Thu Aug 28 2008 SUZUKI Takahiko <takahiko@iij.ad.jp>
- (1.0.0-1)
- public release

* Tue Aug 26 2008 SUZUKI Takahiko <takahiko@iij.ad.jp>
- (0.9.2-1)
- new upstream release

* Fri Aug 22 2008 SUZUKI Takahiko <takahiko@iij.ad.jp>
- (0.9.1-1)
- new upstream release

* Tue Aug 19 2008 Mitsuru Shimamura <simamura@iij.ad.jp>
- (0.9.0-1)
- internal beta release
