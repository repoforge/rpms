# $Id$
# Authority: dag
# Upstream: Morfsta <morfsta$irmplc,com>

Summary: Read EPG information the xmltv site
Name: xmltv2vdr
Version: 1.0.7
Release: 1
License: GPL
Group: Applications/Multimedia
URL: ftp://ftp.cadsoft.de/vdr/Tools/

Source: ftp://ftp.cadsoft.de/vdr/Tools/xmltv2vdr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch

%description
xmltv2vdr allows Electronic Program Guid (EPG) information to be read from
the xmltv site which carries listings for Germany, Finland, US, New Zealand,
UK and SN.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 xmltv2vdr.pl %{buildroot}%{_bindir}/xmltv2vdr

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING HISTORY README grab_freeview_epg.sh examples/
%{_bindir}/xmltv2vdr

%changelog
* Sat Jan 05 2008 Dag Wieers <dag@wieers.com> - 1.0.7-1
- Initial package. (using DAR)
