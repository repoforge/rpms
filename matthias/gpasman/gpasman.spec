# Authority: dag

# Upstream: Olivier Sessink <olivier@bluefish.openoffice.nl>

Summary: A personal password manager for GNOME
Name: gpasman
Version: 1.9.2
Release: 0
Group: Applications/Productivity
License: GPL
URL: http://gpasman.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://gpasman.sourceforge.net/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
Gpasman is a password manager. People working with the internet have to
remember lots of passwords. Saving them in a textfile is not a secure
idea. Gpasman is a GTK solution to this problem since it saves the
password information encrypted, so now you have to remember only one
password instead of ten (or more).

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
desktop-file-install --vendor gnome --delete-original \
	--add-category X-Red-Hat-Base                 \
	--add-category Application                    \
	--add-category Utility                        \
	--dir %{buildroot}%{_datadir}/applications    \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING LICENCE* NEWS README TODO 
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*

%changelog
* Tue Mar 25 2003 Dag Wieers <dag@wieers.com> - 1.9.2-0
- Updated to release 1.9.2.

* Sun Mar 23 2003 Dag Wieers <dag@wieers.com> - 1.9.0-0
- Initial package. (using DAR)
