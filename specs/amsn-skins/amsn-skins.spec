# $Id$

# Authority: dries
# Screenshot: http://amsn.sourceforge.net/shots/contactlist.jpg
# ScreenshotURL: http://amsn.sourceforge.net/modules.php?name=Skins

Summary: Collection of skins for aMSN.
Name: amsn-skins
Version: 0.90
Release: 0
License: GPL
Group: Applications/Internet
URL: http://amsn.sf.net/

Packager: Dries Verachtert <skotty@ulyssis.org>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: http://dl.sf.net/amsn/Bolos.zip
Source1: http://dl.sf.net/amsn/crystola.zip
Source2: http://dl.sf.net/amsn/cubic.zip
Source3: http://dl.sf.net/amsn/MSN.zip
Source4: http://dl.sf.net/amsn/Tux.zip
Source5: http://dl.sf.net/amsn/Fluox.zip
Source6: http://dl.sf.net/amsn/aMac.zip
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

Requires: amsn >= 0.90

%description
amsn is a Tcl/Tk clone that implements the Microsoft Messenger (MSN) for
Unix, Windows, or Macintosh platforms. It supports file transfers,
groups, and many more features.

This package contains a collection of skins.

%prep
%setup -n amsn-skins -c 0 -b 1 -b 2 -b 3 -b 4 -b 5 -b 6

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_datadir}/amsn/skins/
%{__cp} -avx * %{buildroot}%{_datadir}/amsn/skins/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_datadir}/amsn/

%changelog
* Sat Feb 21 2004 Dag Wieers <dag@wieers.com> - 0.90-0
- Initial package. (using DAR)
