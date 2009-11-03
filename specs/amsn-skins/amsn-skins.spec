# $Id$
# Authority: dries

# Screenshot: http://amsn.sf.net/shots/contactlist.jpg
# ScreenshotURL: http://amsn.sf.net/modules.php?name=Skins

# Dist: nodist

Summary: Collection of skins for aMSN
Name: amsn-skins
Version: 0.91
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://amsn.sourceforge.net/

Source0: http://dl.sf.net/amsn/Alloque_Lavender.zip
Source1: http://dl.sf.net/amsn/Alternative-Tux.zip
Source2: http://dl.sf.net/amsn/BSDmsn.zip
Source3: http://dl.sf.net/amsn/Bolos.zip
Source4: http://dl.sf.net/amsn/Fluox.zip
Source5: http://dl.sf.net/amsn/Grey-MSN.zip
Source6: http://dl.sf.net/amsn/Lila.zip
Source7: http://dl.sf.net/amsn/MSN.zip
Source8: http://dl.sf.net/amsn/Rubber.zip
Source9: http://dl.sf.net/amsn/SpherIco.zip
Source10: http://dl.sf.net/amsn/Tux.zip
Source11: http://dl.sf.net/amsn/aDarwin.zip
Source12: http://dl.sf.net/amsn/aMac.zip
Source13: http://dl.sf.net/amsn/crystola.zip
Source14: http://dl.sf.net/amsn/cubic.zip
Source15: http://dl.sf.net/amsn/wolfheart.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: amsn >= 0.91

%description
amsn is a Tcl/Tk clone that implements the Microsoft Messenger (MSN) for
Unix, Windows, or Macintosh platforms. It supports file transfers,
groups, and many more features.

This package contains a collection of skins.

%prep
%setup -n amsn-skins -c 0 -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10 -b 11 -b 12 -b 13 -b 14 -b 15

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_datadir}/amsn/skins/
%{__cp} -apvx * %{buildroot}%{_datadir}/amsn/skins/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_datadir}/amsn/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.91-1.2
- Rebuild for Fedora Core 5.

* Sun May 30 2004 Dag Wieers <dag@wieers.com> - 0.91-1
- Update to newest available aMSN skins.

* Sat Feb 21 2004 Dag Wieers <dag@wieers.com> - 0.90-0
- Initial package. (using DAR)
