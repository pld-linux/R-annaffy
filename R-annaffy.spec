%define		packname	annaffy

Summary:	Annotation tools for Affymetrix biological metadata
Name:		R-%{packname}
Version:	1.30.0
Release:	1
License:	LGPL v2+
Group:		Applications/Engineering
Source0:	http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	706772d7ae0b91168fbf826172af773c
URL:		http://bioconductor.org/packages/release/bioc/html/%{packname}.html
BuildRequires:	R
BuildRequires:	R-Biobase
BuildRequires:	R-GO.db
BuildRequires:	R-KEGG.db
BuildRequires:	R-AnnotationDbi
BuildRequires:	R-hgu95av2.db
BuildRequires:	R-multtest,
BuildRequires:	texlive-latex
BuildRequires:	zlib-devel
Requires:	R
Requires:	R-Biobase
Requires:	R-GO.db
Requires:	R-KEGG.db
Requires:	R-AnnotationDbi
Suggests:	R-hgu95av2.db
Suggests:	R-multtest,
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Functions for handling data from Bioconductor Affymetrix annotation
data packages. Produces compact HTML and text reports including
experimental data and URL links to many online databases. Allows
searching biological metadata using various criteria.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/data
