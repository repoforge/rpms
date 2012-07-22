# ExclusiveDist: el5 el6
Name:       apt-dater
Version:    0.8.6
Release:    1%{?dist}
Summary:	Terminal-based remote package update manager
URL:		http://www.ibh.de/apt-dater/
Source:     http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
License:	GPL
Group:		System/Management
Requires:	screen
Requires:	tcl
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	libxml2-devel
BuildRequires:	ncurses-devel
BuildRequires:	screen
BuildRequires:	tcl-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	perl

%if 0%{?rhel} > 5 
BuildRequires:	popt-devel
%endif

Buildroot:	%{_tmppath}/%{name}-buildroot

%description

apt-dater provides an easy to use ncurses frontend for managing package updates on a large number of remote hosts using SSH.
It supports Debian-based managed hosts as well as OpenSUSE and CentOS based systems.

%prep
%setup
sed "s/manhdir = .*$/manhdir = @docdir@/" man/Makefile.in

%build

%configure --prefix=%{_prefix} --libexec=%{_libexecdir}/apt-dater --disable-rpath --enable-tclfilter --enable-xmlreport --enable-autoref --enable-history --enable-debug

make

%install
(cd src && make install DESTDIR=$RPM_BUILD_ROOT)
(cd lib && make install DESTDIR=$RPM_BUILD_ROOT)
(cd po && make install DESTDIR=$RPM_BUILD_ROOT)
(cd man && make install DESTDIR=$RPM_BUILD_ROOT)
rm $RPM_BUILD_ROOT/usr/share/man/manh/*.html

%clean
rm -rf $RPM_BUILD_ROOT
make clean

%files
%defattr(-,root,root)
%{_bindir}/apt-dater
%dir %{_libdir}/apt-dater
%{_libdir}/apt-dater/*
%doc AUTHORS COPYING ChangeLog README* TODO man/apt-dater.conf.html man/apt-dater.html
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_mandir}/man8/*.8*
%{_datadir}/locale/*/LC_MESSAGES/apt-dater.mo

%changelog
* Thu Feb 02 2012 David Hrbáč <david@hrbac.cz> - 0.8.6-1
- initial build
