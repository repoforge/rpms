# $Id$
# Authority: shuff
# Upstream: Jan Kaluza
# ExcludeDist: el2 el3 el4

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Multi-protocol XMPP transport gateway
Name: spectrum
Version: 1.4.7
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://spectrum.im/

# this changes every release :(
Source: https://github.com/downloads/hanzz/spectrum/spectrum-%{version}.tar.gz
Patch0: spectrum-1.4.7_cmake.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: cmake
BuildRequires: cppunit
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: gloox-devel >= 1.0
BuildRequires: libpurple-devel >= 2.6.0
BuildRequires: poco-devel >= 1.3.3
BuildRequires: python-devel
BuildRequires: python-xmpp
BuildRequires: rpm-macros-rpmforge
BuildRequires: ImageMagick-c++-devel
Requires: logrotate
Requires: python-xmpp

%description
Spectrum is an XMPP transport/gateway. It allows XMPP users to communicate with
their friends who are using one of the supported networks. It supports a wide
range of different networks such as ICQ, XMPP (Jabber, GTalk), AIM, MSN,
Facebook, Twitter, Gadu-Gadu, IRC and SIMPLE. Spectrum is written in C++ and
uses the Gloox XMPP library and libpurple for "legacy networks".

%prep
%setup
%{?el5:%patch0 -p1}

%build
%cmake .
%{__make} %{?_smp_mflags}

# make spectrumctl
(cd spectrumctl && %{__python} setup.py build)

# make a logrotate file
cat <<LOGROTATE >spectrum-logrotate
/var/log/spectrum/*.log {
    rotate 5
    size 1M
    missingok
    notifempty
}
LOGROTATE

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# install spectrumctl
(cd spectrumctl && %{__python} setup.py install --root %{buildroot} --prefix %{_prefix})
%{__chmod} 755 %{buildroot}/%{_bindir}/spectrumctl

# install some additional stuff
%{__install} -D -m 644 schemas/mysql_schema.sql %{buildroot}%{_datadir}/spectrum/schemas/mysql_schema.sql
%{__install} -D -m 755 initscripts/fedora/spectrum %{buildroot}%{_initddir}/spectrum
%{__install} -D -m 644 spectrum-logrotate %{buildroot}%{_sysconfdir}/logrotate.d/spectrum
%{__install} -d -m 644 %{buildroot}%{_localstatedir}/{lib,run,log}/spectrum

# daemon goes in sbin
%{__install} -d -m755 %{buildroot}%{_sbindir}
%{__mv} %{buildroot}%{_bindir}/spectrum %{buildroot}%{_sbindir}

# config file example goes in docdir
%{__mv} %{buildroot}%{_sysconfdir}/spectrum/spectrum.cfg.example .

%find_lang %{name}

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%pre
if [ $1 = 0 ]; then
    /usr/sbin/groupadd -r spectrum
    /usr/sbin/useradd -r -g spectrum -d %{_localstatedir}/lib/spectrum \
        -s /sbin/nologin \
        -c "spectrum XMPP transport" \
        spectrum
    exit 0
fi

%post
/sbin/chkconfig --add spectrum
exit 0

%preun
if [ $1 = 0 ]; then
    /sbin/service spectrum stop >/dev/null 2>&1
    /sbin/chkconfig --del spectrum
    exit 0
fi

%postun 
if [ $1 >= 0 ]; then
    /sbin/service spectrum condrestart >/dev/null 2>&1
    exit 0
fi

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING TODO spectrum.cfg.example
%doc %{_mandir}/man?/*
%{python_sitelib}/*
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/spectrum/
%{_initddir}/spectrum
%attr(700, spectrum, spectrum) %{_localstatedir}/lib/spectrum
%attr(700, spectrum, spectrum) %{_localstatedir}/run/spectrum
%attr(700, spectrum, spectrum) %{_localstatedir}/log/spectrum
%attr(750, root, spectrum) %dir %{_sysconfdir}/spectrum
%config(noreplace) %{_sysconfdir}/logrotate.d/spectrum

%changelog
* Wed Aug 03 2011 Steve Huff <shuff@vecna.org> - 1.4.7-1
- Initial package (ported from EPEL).

