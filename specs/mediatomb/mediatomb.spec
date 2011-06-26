# $Id$
# Authority: shuff
# Upstream:  Sergey Bostandzhyan <contact$mediatomb,cc>

Summary: UPnP server with web interface
Name: mediatomb
Version: 0.12.1
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://mediatomb.cc/

Source: http://downloads.sourceforge.net/project/mediatomb/MediaTomb/%{version}/mediatomb-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#Buildarch: noarch
BuildRequires: binutils
BuildRequires: expat-devel 
BuildRequires: file-devel 
BuildRequires: ffmpeg-devel
BuildRequires: gcc-c++
BuildRequires: js-devel
# BuildRequires: lastfmlib-devel
BuildRequires: libcurl-devel >= 4
BuildRequires: libexif-devel
# BuildRequires: libffmpegthumbnailer-devel
BuildRequires: libssh2-devel
BuildRequires: nspr-devel
BuildRequires: make
BuildRequires: mysql-devel >= 4
BuildRequires: rpm-macros-rpmforge
BuildRequires: sqlite-devel >= 3
BuildRequires: taglib-devel
BuildRequires: zlib-devel

%description
MediaTomb is an open source (GPL) UPnP MediaServer with a nice web user
interface, it allows you to stream your digital media through your home network
and listen to/watch it on a variety of UPnP compatible devices.

MediaTomb implements the UPnP MediaServer V 1.0 specification that can be found
on http://www.upnp.org/. The current implementation focuses on parts that are
required by the specification, however we look into extending the functionality
to cover the optional parts of the spec as well.

MediaTomb should work with any UPnP compliant MediaRenderer, please tell us if
you experience difficulties with particular models, also take a look at the
Supported Devices list for more information. 


%prep
%setup

%build
%configure \
    --disable-dependency-tracking \
    --enable-ffmpeg \
    --with-search=%{_usr}
%{__make} %{?_smp_mflags}

# fix mediatomb init script
%{__perl} -pi -e 's|/etc/mediatomb\.conf|/etc/sysconfig/mediatomb|;' scripts/mediatomb-service-fedora 

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# init script
%{__install} -d -m755 %{buildroot}%{_initrddir}
%{__install} -m755 scripts/mediatomb-service-fedora %{buildroot}%{_initrddir}/mediatomb

# config file
%{__install} -d -m755 %{buildroot}%{_sysconfdir}/sysconfig
%{__install} -m755 config/mediatomb-conf-fedora %{buildroot}%{_sysconfdir}/sysconfig/mediatomb

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%post
if [ $1 -eq 1 ]; then
    /usr/sbin/useradd -d %{_datadir}/mediatomb -U -r -s /bin/false mediatomb
    /sbin/chkconfig --add mediatomb
    exit 0
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/chkconfig --del mediatomb
    /usr/sbin/userdel mediatomb
    exit 0
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README* TODO doc/ scripts/
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/mediatomb/
%{_initrddir}/mediatomb
%config %{_sysconfdir}/sysconfig/mediatomb

%changelog
* Sat Jun 25 2011 Steve Huff <shuff@vecna.org> - 0.12.1-1
- Initial package.
