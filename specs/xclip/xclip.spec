# $Id$
# Authority: shuff
# Upstream: Peter Åstrand <astrand$lysator.liu.se>

Summary: Access X11 clipboard from the command line
Name: xclip
Version: 0.12
Release: 1%{?dist}
License: GPL
Group: Applications/X11
URL: http://xclip.sourceforge.net/

Source: http://downloads.sourceforge.net/xclip/xclip-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libXmu-devel, imake
BuildRequires: autoconf, automake

%description
xclip is a command line interface to the X11 clipboard. It can also be used for
copying files, as an alternative to sftp/scp, thus avoiding password prompts
when X11 forwarding has already been setup.

%prep
%setup

%build
%configure 
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README 
%{_bindir}/*
%dir %{_mandir}/man1/
%{_mandir}/man1/*

%changelog
* Tue Oct 27 2009 Steve Huff <shuff@vecna.org> - 0.12-1
- Initial package.
