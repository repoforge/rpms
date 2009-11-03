# $Id$
# Upstream: Peter Willis <peterwwillis$yahoo,com>
# Authority: dries

Summary: Perl script that downloads MP3s off MySpace.com
Name: getmsmp3 
Version: 0.4
Release: 1%{?dist}
License: WTFPL 
Group: Applications/Internet
URL: http://psydev.sourceforge.net/new/misc/getmsmp3

Source: http://psydev.sourceforge.net/new/misc/getmsmp3
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
Requires: perl >= 5.8.8

%description
Getmsmp3 is a small Perl script that downloads MP3s off of
MySpace profiles (including band playlists) to the current 
directory. The source code is released under the DO WHAT 
THE FUCK YOU WANT TO PUBLIC LICENSE :-)

%prep
%setup -c -T

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -p -m0755 -D %{SOURCE0} %{buildroot}%{_bindir}/getmsmp3

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/getmsmp3

%changelog
* Sat Jul 26 2008 Sven Aluoor <aluoor@gmail.com> - 0.4
- Initial package.
