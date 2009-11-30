# $Id$
# Authority: shuff
# Upstream: Rick Richardson <http://foo2zjs.rkkda.com/forum/index.php>
# ExclusiveDist: el5

# Note: apparently this cannot work with Ghostscript 8.64

Summary: a linux printer driver for ZjStream protocol
Name: foo2zjs
Version: 1.20.20091112
Release: 1%{?dist}
License: GPL
Group: Applications/Text
URL: http://foo2zjs.rkkda.com/

Source: http://foo2zjs.rkkda.com/%{name}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils, gcc, make
BuildRequires: coreutils
BuildRequires: /usr/bin/ex
BuildRequires: ghostscript
BuildRequires: foomatic
BuildRequires: wget
BuildRequires: initscripts
Requires: cups
Requires: ghostscript
Requires: foomatic
Requires: initscripts

Provides: foo2zjs
Provides: foo2hp
Provides: foo2xqx
Provides: foo2lava
Provides: foo2qpdl
Provides: foo2slx
Provides: foo2hiperc
Provides: foo2oak

%description
foo2zjs is an open source printer driver for printers that use the Zenographics
ZjStream wire protocol for their print data, such as the HP Color LaserJet
2600n and the HP Color LaserJet CP1215. These printers are often erroneously
referred to as winprinters or GDI printers. However, Microsoft GDI only
mandates the API between an application and the printer driver, not the
protocol on the wire between the printer driver and the printer. In fact,
ZjStream printers are raster printers which happen to use a very efficient wire
protocol which was developed by Zenographics and licensed by most major printer
manufacturers for at least some of their product lines. ZjStream is just one of
many wire protocols that are in use today, such as Postscript, PCL, Epson, etc. 


%prep
%setup -n foo2zjs

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

# download additional printer information
for model in "1215 1500 1600 2600n 1600w 1680 1690 2480 2490 2530 4690 6115 cpwl 2200 2300 2430 300 315 600 610 2160 3160 6110 500 3200 3300 3400 3530 5100 5200 5500 5600 5800 1000 1005 1018 1020 P1005 P1006 P1007 P1008 P1505"; do
    ./getweb ${model}
done

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

# put usb_printerid in %{_bindir}
%{__mv} %{buildroot}/bin/* %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/service cups restart

%postun
/sbin/service cups restart

%files
%defattr(-, root, root, 0755)
%doc manual.pdf COPYING INSTALL README ChangeLog
%doc %{_mandir}/man?/*
%exclude %{_docdir}
%{_bindir}/*
%{_datadir}/foo*

%changelog
* Mon Nov 30 2009 Steve Huff <shuff@vecna.org> - 1.20.20091112-1
- Initial package.
