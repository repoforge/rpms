# Authority: freshrpms
Summary: The GNOME disk catalog.
Name: gtktalog
Version: 1.0.1
Release: 0
License: GPL
Group: Applications/Archiving
URL: http://www.freesoftware.fsf.org/gtktalog/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://freesoftware.fsf.org/download/gtktalog/gtktalog/sources/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


Requires: gnome-libs zlib

%description
GTKtalog is a disk catalog, it means you can use it to create a really small
database with images of files and folders of your CD-rom. So you can browse all
your CD's very quickly, see contents of certain files (tar.gz, rpm files ...).
You can give to each folder and file a category and a description. You can
search for files in your database with filename, category, description or file
information parameter, and find in which CD the file you are looking for is.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README TODO
%doc Docs/README.catalog3 Docs/README.data_representation Docs/README.Linux
%doc %{_mandir}/man?/*
%doc %{_datadir}/gnome/help/gtktalog/*
%{_bindir}/gtktalog
%{_libdir}/gtktalog/*
%{_datadir}/gnome/apps/Applications/gtktalog.desktop
%{_datadir}/gtktalog/*
%{_datadir}/pixmaps/gtktalog*.png

%changelog
* Mon Apr 14 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Updated to release 1.0.1.

* Sun Oct 13 2002 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0.

* Mon Dec 18 2000 Yves Mettier <ymettier@libertysurf.fr>
- Many changed thanks to Matthias Saou <matthias.saou@est.une.marmotte.net>

* Tue Nov 14 2000 Yves Mettier <ymettier@libertysurf.fr>
- I'm using mdk-7.2 and all major rpm-distributions seem to have rpm-4.x
  So I'm getting rid of some unuseful stuff.

* Sun Sep 24 2000 Yves Mettier <ymettier@libertysurf.fr>
- Updated to rpm 3.0.5 because there was some problems with the prefix.

* Sun Aug 20 2000 Yves Mettier <ymettier@libertysurf.fr>
- removed ncatalog

* Fri Aug 04 2000 Yves Mettier <ymettier@libertysurf.fr>
- Now needs zlib

* Sun Jul 16 2000 Yves Mettier <ymettier@libertysurf.fr>
- separation of ncatalog

* Tue Jun 20 2000 Yves Mettier <ymettier@libertysurf.fr>
- First spec file

