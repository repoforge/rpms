# Authority: dag
# Upstream: Chris Ladd <caladd@particlestorm.net>

Summary: Graphical secure password generator.
Name: gnome-password-generator
Version: 1.0
Release: 1
License: GPL
Group: Applications/
URL: http://gnome-password.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/gnome-password/gnome-password-generator-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch: noarch
BuildRequires: python >= 2.0, pygtk2-devel, gnome-python2
Requires: python >= 2.0, pygtk2, gnome-python2

%description
Gnome Password Generator is a graphical secure password generator.
It allows the user to generate a specified number of random
passwords of a specified length.

%prep
%setup

%{__perl} -pi.orig -e '
		s|/usr/bin|%{buildroot}%{_bindir}|g;
		s|/usr/share|%{buildroot}%{_datadir}|g;
		s|^chown|#chown|;
	' install.sh

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_datadir}/{applications,pixmaps}/
sh install.sh

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL README
%{_bindir}/*
%{_datadir}/pixmaps/*.svg
%{_datadir}/applications/*.desktop

%changelog
#- Changed BuildArch to noarch.

* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
